###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Sandbox

Application sandbox environment.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef enum SDL_Sandbox
{
    SDL_SANDBOX_NONE = 0,
    SDL_SANDBOX_UNKNOWN_CONTAINER,
    SDL_SANDBOX_FLATPAK,
    SDL_SANDBOX_SNAP,
    SDL_SANDBOX_MACOS
} SDL_Sandbox;
```

## Version

This enum is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySystem](CategorySystem)

