# SDL_GetOpenHarmonySDKVersion

Query OpenHarmony API level of the current device.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_GetOpenHarmonySDKVersion(void);
```

## Return Value

(int) Returns the OpenHarmony API level.

## Remarks

- API level 20: OpenHarmony 6.0.0
- API level 18: OpenHarmony 5.1.0
- API level 16: OpenHarmony 5.0.4
- API level 15: OpenHarmony 5.0.3
- API level 14: OpenHarmony 5.0.2
- API level 13: OpenHarmony 5.0.1
- API level 12: OpenHarmony 5.0.0
- API level 11: OpenHarmony 4.1.0
- API level 10: OpenHarmony 4.0.0
- API level 9: OpenHarmony 3.2.0

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

