###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowPosition

Set the position of a window, in screen coordinates.

## Syntax

```c
int SDL_SetWindowPosition(SDL_Window *window, int x, int y);

```

## Function Parameters

|                |                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window to reposition                                                                                                                      |
| **x**          | the x coordinate of the window, or `[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED)` or `[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED)` |
| **y**          | the y coordinate of the window, or `[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED)` or `[SDL_WINDOWPOS_UNDEFINED](SDL_WINDOWPOS_UNDEFINED)` |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowPosition](SDL_GetWindowPosition)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


