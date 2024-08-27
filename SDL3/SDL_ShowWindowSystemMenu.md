###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowWindowSystemMenu

Display the system-level window menu.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_ShowWindowSystemMenu(SDL_Window *window, int x, int y);
```

## Function Parameters

|                            |            |                                                                                     |
| -------------------------- | ---------- | ----------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window for which the menu will be displayed.                                    |
| int                        | **x**      | the x coordinate of the menu, relative to the origin (top-left) of the client area. |
| int                        | **y**      | the y coordinate of the menu, relative to the origin (top-left) of the client area. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

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
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

