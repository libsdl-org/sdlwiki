###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetAndroidSDKVersion

Query Android API level of the current device.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_GetAndroidSDKVersion(void);

```

## Return Value

Returns the Android API level.

## Remarks

- API level 31: Android 12
- API level 30: Android 11
- API level 29: Android 10
- API level 28: Android 9
- API level 27: Android 8.1
- API level 26: Android 8.0
- API level 25: Android 7.1
- API level 24: Android 7.0
- API level 23: Android 6.0
- API level 22: Android 5.1
- API level 21: Android 5.0
- API level 20: Android 4.4W
- API level 19: Android 4.4
- API level 18: Android 4.3
- API level 17: Android 4.2
- API level 16: Android 4.1
- API level 15: Android 4.0.3
- API level 14: Android 4.0
- API level 13: Android 3.2
- API level 12: Android 3.1
- API level 11: Android 3.0
- API level 10: Android 2.3.3

## Version

This function is available since SDL 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

