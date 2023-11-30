###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreatePopupWindow

Create a child popup window of the specified parent window.

## Syntax

```c
SDL_Window* SDL_CreatePopupWindow(SDL_Window *parent, int offset_x, int offset_y, int w, int h, Uint32 flags);

```

## Function Parameters

|                  |                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **parent**       | the parent of the window, must not be NULL                                                                                                                           |
| **offset_x**     | the x position of the popup window relative to the origin of the parent                                                                                              |
| **offset_y**     | the y position of the popup window relative to the origin of the parent window                                                                                       |
| **w**            | the width of the window                                                                                                                                              |
| **h**            | the height of the window                                                                                                                                             |
| **flags**        | [SDL_WINDOW_TOOLTIP](SDL_WINDOW_TOOLTIP) or [SDL_WINDOW_POPUP](SDL_WINDOW_POPUP) MENU, and zero or more additional [SDL_WindowFlags](SDL_WindowFlags) OR'd together. |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

'flags' **must** contain exactly one of the following: -
'[SDL_WINDOW_TOOLTIP](SDL_WINDOW_TOOLTIP)': The popup window is a tooltip
and will not pass any input events. -
'[SDL_WINDOW_POPUP_MENU](SDL_WINDOW_POPUP_MENU)': The popup window is a
popup menu. The topmost popup menu will implicitly gain the keyboard focus.

The following flags are not relevant to popup window creation and will be
ignored:

- '[SDL_WINDOW_MINIMIZED](SDL_WINDOW_MINIMIZED)'
- '[SDL_WINDOW_MAXIMIZED](SDL_WINDOW_MAXIMIZED)'
- '[SDL_WINDOW_FULLSCREEN](SDL_WINDOW_FULLSCREEN)'
- '[SDL_WINDOW_BORDERLESS](SDL_WINDOW_BORDERLESS)'

The parent parameter **must** be non-null and a valid window. The parent of
a popup window can be either a regular, toplevel window, or another popup
window.

Popup windows cannot be minimized, maximized, made fullscreen, raised,
flash, be made a modal window, be the parent of a modal window, or grab the
mouse and/or keyboard. Attempts to do so will fail.

Popup windows implicitly do not have a border/decorations and do not appear
on the taskbar/dock or in lists of windows such as alt-tab menus.

If a parent window is hidden, any child popup windows will be recursively
hidden as well. Child popup windows not explicitly hidden will be restored
when the parent is shown.

If the parent window is destroyed, any child popup windows will be
recursively destroyed as well.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties)
* [SDL_DestroyWindow](SDL_DestroyWindow)
* [SDL_GetWindowParent](SDL_GetWindowParent)

----
[CategoryAPI](CategoryAPI)

