###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPowerInfo

Get the current power supply details.

## Header File

Defined in [<SDL3/SDL_power.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_power.h)

## Syntax

```c
SDL_PowerState SDL_GetPowerInfo(int *seconds, int *percent);
```

## Function Parameters

|       |             |                                                                                                                                                                                       |
| ----- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| int * | **seconds** | a pointer filled in with the seconds of battery life left, or NULL to ignore. This will be filled in with -1 if we can't determine a value or there is no battery.                    |
| int * | **percent** | a pointer filled in with the percentage of battery life left, between 0 and 100, or NULL to ignore. This will be filled in with -1 we can't determine a value or there is no battery. |

## Return Value

([SDL_PowerState](SDL_PowerState)) Returns the current battery state or
[`SDL_POWERSTATE_ERROR`](SDL_POWERSTATE_ERROR) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You should never take a battery status as absolute truth. Batteries
(especially failing batteries) are delicate hardware, and the values
reported here are best estimates based on what that hardware reports. It's
not uncommon for older batteries to lose stored power much faster than it
reports, or completely drain when reporting it has 20 percent left, etc.

Battery status can change at any time; if you are concerned with power
state, you should call this function frequently, and perhaps ignore changes
until they seem to be stable for a few seconds.

It's possible a platform can only report battery percentage or time left
but not both.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
int secs, pct;
if (SDL_GetPowerInfo(&secs, &pct) == SDL_POWERSTATE_ON_BATTERY) {
    printf("Battery is draining: ");
    if (secs == -1) {
        printf("(unknown time left)\n");
    } else {
        printf("(%d seconds left)\n", secs);
    }

    if (pct == -1) {
        printf("(unknown percentage left)\n");
    } else {
        printf("(%d percent left)\n", pct);
    }
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPower](CategoryPower)

