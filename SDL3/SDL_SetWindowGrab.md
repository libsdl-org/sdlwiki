###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowGrab

Set a window's input grab mode.

## Syntax

```c
int SDL_SetWindowGrab(SDL_Window *window, SDL_bool grabbed);

```

## Function Parameters

|                 |                                                                               |
| --------------- | ----------------------------------------------------------------------------- |
| **window**      | the window for which the input grab mode should be set                        |
| **grabbed**     | [SDL_TRUE](SDL_TRUE.md) to grab input or [SDL_FALSE](SDL_FALSE.md) to release input |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

When input is grabbed, the mouse is confined to the window. This function
will also grab the keyboard if
[`SDL_HINT_GRAB_KEYBOARD`](SDL_HINT_GRAB_KEYBOARD) is set. To grab the
keyboard without also grabbing the mouse, use
[SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab.md)().

If the caller enables a grab while another window is currently grabbed, the
other window loses its grab in favor of the caller's window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGrabbedWindow](SDL_GetGrabbedWindow.md)
* [SDL_GetWindowGrab](SDL_GetWindowGrab.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
