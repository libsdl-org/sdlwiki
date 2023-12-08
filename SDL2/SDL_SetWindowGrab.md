###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowGrab

Set a window's input grab mode.

## Syntax

```c
void SDL_SetWindowGrab(SDL_Window * window,
                       SDL_bool grabbed);

```

## Function Parameters

|                 |                                                                               |
| --------------- | ----------------------------------------------------------------------------- |
| **window**      | the window for which the input grab mode should be set                        |
| **grabbed**     | [SDL_TRUE](SDL_TRUE.md) to grab input or [SDL_FALSE](SDL_FALSE.md) to release input |

## Remarks

When input is grabbed, the mouse is confined to the window. This function
will also grab the keyboard if
[`SDL_HINT_GRAB_KEYBOARD`](SDL_HINT_GRAB_KEYBOARD) is set. To grab the
keyboard without also grabbing the mouse, use
[SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab.md)().

If the caller enables a grab while another window is currently grabbed, the
other window loses its grab in favor of the caller's window.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetGrabbedWindow](SDL_GetGrabbedWindow.md)
* [SDL_GetWindowGrab](SDL_GetWindowGrab.md)

----
[CategoryAPI](CategoryAPI.md)
