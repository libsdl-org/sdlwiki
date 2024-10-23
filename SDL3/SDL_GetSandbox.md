###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetSandbox

Get the application sandbox environment, if any.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
SDL_Sandbox SDL_GetSandbox(void);
```

## Return Value

([SDL_Sandbox](SDL_Sandbox)) Returns the application sandbox environment or
[SDL_SANDBOX_NONE](SDL_SANDBOX_NONE) if the application is not running in a
sandbox environment.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

