###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RemoveTimer

Remove a timer created with [SDL_AddTimer](SDL_AddTimer)().

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_RemoveTimer(SDL_TimerID id);

```

## Function Parameters

|            |                               |
| ---------- | ----------------------------- |
| **id**     | the ID of the timer to remove |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the timer is removed or
[SDL_FALSE](SDL_FALSE) if the timer wasn't found.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_AddTimer](SDL_AddTimer)


## Example

```c
// Function to be called after a certain time

Uint32 callback(Uint32 interval, void* name) {

    printf("Hello %s!\n", (const char*)name);
       
    return 0;
}

/* ... */

// Initialize timer

if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER) < 0) {
  SDL_Log("SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER) failed: %s", SDL_GetError());
}

/* ... */

// Set timer to 1 second

SDL_TimerID timerID = SDL_AddTimer(1000, callback, "SDL");

// Main loop

SDL_bool quit;
while(!quit) {
    /* ... */
}

// Remove timer after main loop

SDL_RemoveTimer(timerID);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

