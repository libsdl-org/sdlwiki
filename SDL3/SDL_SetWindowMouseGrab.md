###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowMouseGrab

Set a window's mouse grab mode.

## Syntax

```c
int SDL_SetWindowMouseGrab(SDL_Window *window, SDL_bool grabbed);

```

## Function Parameters

|                 |                                                                                    |
| --------------- | ---------------------------------------------------------------------------------- |
| **window**      | The window for which the mouse grab mode should be set.                            |
| **grabbed**     | This is [SDL_TRUE](SDL_TRUE) to grab mouse, and [SDL_FALSE](SDL_FALSE) to release. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Mouse grab confines the mouse cursor to the window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowMouseGrab](SDL_GetWindowMouseGrab)
* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)
* [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI)

