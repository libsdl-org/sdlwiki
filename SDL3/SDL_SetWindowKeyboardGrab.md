###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowKeyboardGrab

Set a window's keyboard grab mode.

## Syntax

```c
int SDL_SetWindowKeyboardGrab(SDL_Window *window, SDL_bool grabbed);

```

## Function Parameters

|                 |                                                                                       |
| --------------- | ------------------------------------------------------------------------------------- |
| **window**      | The window for which the keyboard grab mode should be set.                            |
| **grabbed**     | This is [SDL_TRUE](SDL_TRUE) to grab keyboard, and [SDL_FALSE](SDL_FALSE) to release. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Keyboard grab enables capture of system keyboard shortcuts like Alt+Tab or
the Meta/Super key. Note that not all system keyboard shortcuts can be
captured by applications (one example is Ctrl+Alt+Del on Windows).

This is primarily intended for specialized applications such as VNC clients
or VM frontends. Normal games should not use keyboard grab.

When keyboard grab is enabled, SDL will continue to handle Alt+Tab when the
window is full-screen to ensure the user is not trapped in your
application. If you have a custom keyboard shortcut to exit fullscreen
mode, you may suppress this behavior with
[`SDL_HINT_ALLOW_ALT_TAB_WHILE_GRABBED`](SDL_HINT_ALLOW_ALT_TAB_WHILE_GRABBED).

If the caller enables a grab while another window is currently grabbed, the
other window loses its grab in favor of the caller's window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowKeyboardGrab](SDL_GetWindowKeyboardGrab)
* [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
* [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI)

