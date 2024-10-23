###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowKeyboardGrab

Set a window's keyboard grab mode.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowKeyboardGrab(SDL_Window *window, bool grabbed);
```

## Function Parameters

|                            |             |                                                            |
| -------------------------- | ----------- | ---------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**  | the window for which the keyboard grab mode should be set. |
| bool                       | **grabbed** | this is true to grab keyboard, and false to release.       |

## Return Value

(bool) Returns true on success or false on failure; call
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

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowKeyboardGrab](SDL_GetWindowKeyboardGrab)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

