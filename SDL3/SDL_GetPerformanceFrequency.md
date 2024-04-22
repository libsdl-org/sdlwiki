###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPerformanceFrequency

Get the count per second of the high resolution counter.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
Uint64 SDL_GetPerformanceFrequency(void);

```

## Return Value

Returns a platform-specific count per second.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include <SDL3/SDL.h>

#define DEFAULT_RESOLUTION  1

static int ticks = 0;

static Uint32 SDLCALL
ticktock(Uint32 interval, void *param)
{
    ++ticks;
    return (interval);
}

static Uint32 SDLCALL
callback(Uint32 interval, void *param)
{
    SDL_Log("Timer %d : param = %d", interval, (int) (uintptr_t) param);
    return interval;
}

int
main(int argc, char *argv[])
{
    int i, desired;
    SDL_TimerID t1, t2, t3;
    Uint32 start32, now32;
    Uint64 start, now;

    /* Enable standard application logging */
    SDL_LogSetPriority(SDL_LOG_CATEGORY_APPLICATION, SDL_LOG_PRIORITY_INFO);

    if (SDL_Init(SDL_INIT_TIMER) < 0) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't initialize SDL: %s", SDL_GetError());
        return (1);
    }

    /* Start the timer */
    desired = 0;
    if (argv[1]) {
        desired = SDL_atoi(argv[1]);
    }
    if (desired == 0) {
        desired = DEFAULT_RESOLUTION;
    }
    t1 = SDL_AddTimer(desired, ticktock, NULL);

    /* Wait 10 seconds */
    SDL_Log("Waiting 10 seconds");
    SDL_Delay(10 * 1000);

    /* Stop the timer */
    SDL_RemoveTimer(t1);

    /* Print the results */
    if (ticks) {
        SDL_Log("Timer resolution: desired = %d ms, actual = %f ms",
                desired, (double) (10 * 1000) / ticks);
    }

    /* Test multiple timers */
    SDL_Log("Testing multiple timers...");
    t1 = SDL_AddTimer(100, callback, (void *) 1);
    if (!t1)
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION,"Could not create timer 1: %s", SDL_GetError());
    t2 = SDL_AddTimer(50, callback, (void *) 2);
    if (!t2)
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION,"Could not create timer 2: %s", SDL_GetError());
    t3 = SDL_AddTimer(233, callback, (void *) 3);
    if (!t3)
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION,"Could not create timer 3: %s", SDL_GetError());

    /* Wait 10 seconds */
    SDL_Log("Waiting 10 seconds");
    SDL_Delay(10 * 1000);

    SDL_Log("Removing timer 1 and waiting 5 more seconds");
    SDL_RemoveTimer(t1);

    SDL_Delay(5 * 1000);

    SDL_RemoveTimer(t2);
    SDL_RemoveTimer(t3);

    start = SDL_GetPerformanceCounter();
    for (i = 0; i < 1000000; ++i) {
        ticktock(0, NULL);
    }
    now = SDL_GetPerformanceCounter();
    SDL_Log("1 million iterations of ticktock took %f ms", (double)((now - start)*1000) / SDL_GetPerformanceFrequency());

    SDL_Log("Performance counter frequency: %"SDL_PRIu64"", (unsigned long long) SDL_GetPerformanceFrequency());
    start32 = SDL_GetTicks();
    start = SDL_GetPerformanceCounter();
    SDL_Delay(1000);
    now = SDL_GetPerformanceCounter();
    now32 = SDL_GetTicks();
    SDL_Log("Delay 1 second = %d ms in ticks, %f ms according to performance counter", (now32-start32), (double)((now - start)*1000) / SDL_GetPerformanceFrequency());

    SDL_Quit();
    return (0);
}
```

## See Also

* [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)


