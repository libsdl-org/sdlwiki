###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowMouseGrab

Set a window's mouse grab mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowMouseGrab(SDL_Window * window,
                            SDL_bool grabbed);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **window**      | The window for which the mouse grab mode should be set.                            |
| **grabbed**     | This is [SDL_TRUE](SDL_TRUE) to grab mouse, and [SDL_FALSE](SDL_FALSE) to release. |

## Remarks

Mouse grab confines the mouse cursor to the window.

## Version

This function is available since SDL 2.0.16.

## See Also

* [SDL_GetWindowMouseGrab](SDL_GetWindowMouseGrab)
* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)
* [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

