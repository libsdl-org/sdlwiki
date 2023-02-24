###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowKeyboardGrab

Get a window's keyboard grab mode.

## Syntax

```c
SDL_bool SDL_GetWindowKeyboardGrab(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if keyboard is grabbed, and
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.16.

## Related Functions

* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)
* [SDL_GetWindowGrab](SDL_GetWindowGrab)

----
[CategoryAPI](CategoryAPI)

