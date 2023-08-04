###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowWindowSystemMenu

Display the system-level window menu.

## Syntax

```c
int SDL_ShowWindowSystemMenu(SDL_Window *window, int x, int y);

```

## Function Parameters

|                |                                                                                    |
| -------------- | ---------------------------------------------------------------------------------- |
| **window**     | the window for which the menu will be displayed                                    |
| **x**          | the x coordinate of the menu, relative to the origin (top-left) of the client area |
| **y**          | the y coordinate of the menu, relative to the origin (top-left) of the client area |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This default window menu is provided by the system and on some platforms
provides functionality for setting or changing privileged state on the
window, such as moving it between workspaces or displays, or toggling the
always-on-top property.

On platforms or desktops where this is unsupported, this function does
nothing.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

