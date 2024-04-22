###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPowerInfo

Get the current power supply details.

## Header File

Defined in [SDL_power.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_power.h)

## Syntax

```c
SDL_PowerState SDL_GetPowerInfo(int *seconds, int *percent);

```

## Function Parameters

|                 |                                                                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **seconds**     | seconds of battery life left, you can pass a NULL here if you don't care, will return -1 if we can't determine a value, or we're not running on a battery                       |
| **percent**     | percentage of battery life left, between 0 and 100, you can pass a NULL here if you don't care, will return -1 if we can't determine a value, or we're not running on a battery |

## Return Value

Returns an [SDL_PowerState](SDL_PowerState) enum representing the current
battery state.

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

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

