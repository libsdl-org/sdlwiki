###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasJoystick

Return whether a joystick is currently connected.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_bool SDL_HasJoystick(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if a joystick is connected,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetJoysticks](SDL_GetJoysticks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

