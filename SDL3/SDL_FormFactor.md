# SDL_FormFactor

The possible form factors for a device.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef enum SDL_FormFactor {
    SDL_FORMFACTOR_UNKNOWN = 0,
    SDL_FORMFACTOR_DESKTOP,
    SDL_FORMFACTOR_LAPTOP,
    SDL_FORMFACTOR_PHONE,
    SDL_FORMFACTOR_TABLET,
    SDL_FORMFACTOR_CONSOLE,
    SDL_FORMFACTOR_HANDHELD,
    SDL_FORMFACTOR_WATCH,
    SDL_FORMFACTOR_TV,
    SDL_FORMFACTOR_HEADSET,
    SDL_FORMFACTOR_CAR
} SDL_FormFactor;
```

## Version

This enum is available since SDL 3.4.0.

## See Also

- [SDL_GetDeviceFormFactor](SDL_GetDeviceFormFactor)
- [SDL_GetDeviceFormFactorName](SDL_GetDeviceFormFactorName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySystem](CategorySystem)

