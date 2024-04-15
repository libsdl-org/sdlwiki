###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsMouseHaptic

Query whether or not the current mouse has haptic capabilities.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_bool SDL_IsMouseHaptic(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the mouse is haptic or
[SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_OpenHapticFromMouse](SDL_OpenHapticFromMouse)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

