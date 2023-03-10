###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePopupWindow

Create a child popup window of the specified parent window.

## Syntax

```c
SDL_Window* SDL_CreatePopupWindow(SDL_Window *parent, int offset_x, int offset_y, int w, int h, Uint32 flags);

```

## Function Parameters

|                  |                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **parent**       | the parent of the window, must not be NULL                                                            |
| **offset_x**     | the x position of the popup window relative to the origin of the parent, in screen coordinates        |
| **offset_y**     | the y position of the popup window relative to the origin of the parent window, in screen coordinates |
| **w**            | the width of the window, in screen coordinates                                                        |
| **h**            | the height of the window, in screen coordinates                                                       |
| **flags**        | 0, or one or more [SDL_WindowFlags](SDL_WindowFlags) OR'd together                                    |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

'flags' **must** contain exactly one of the following: -
'[SDL_WINDOW_TOOLTIP](SDL_WINDOW_TOOLTIP)': The popup window is a tooltip
and will not pass any input events -
'[SDL_WINDOW_POPUP_MENU](SDL_WINDOW_POPUP_MENU)': The popup window is a
popup menu

The following flags are not valid for popup windows and will be ignored: -
'[SDL_WINDOW_MINIMIZED](SDL_WINDOW_MINIMIZED)' -
'[SDL_WINDOW_MAXIMIZED](SDL_WINDOW_MAXIMIZED)' -
'[SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN)' -
[`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS) -
[`SDL_WINDOW_MOUSE_GRABBED`](SDL_WINDOW_MOUSE_GRABBED)

The parent parameter **must** be non-null and a valid window. The parent of
a popup window can be either a regular, toplevel window, or another popup
window.

Popup windows cannot be minimized, maximized, made fullscreen, or grab the
mouse. Attempts to do so will fail.

If a parent window is hidden, any child popup windows will be recursively
hidden as well. Child popup windows not explicitly hidden will be restored
when the parent is shown.

If the parent window is destroyed, any child popup windows will be
recursively destroyed as well.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI)

