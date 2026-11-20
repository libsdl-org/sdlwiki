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

## Remarks

Note that a sandbox type of
[`SDL_SANDBOX_UNKNOWN_CONTAINER`](SDL_SANDBOX_UNKNOWN_CONTAINER) does not
necessarily imply that the container acts a security boundry.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

