###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetShapedWindowMode

Get the shape parameters of a shaped window.

## Syntax

```c
int SDL_GetShapedWindowMode(SDL_Window *window,SDL_WindowShapeMode *shape_mode);

```

## Function Parameters

|                    |                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------- |
| **window**         | The shaped window whose parameters should be retrieved.                                 |
| **shape_mode**     | An empty shape-mode structure to fill, or NULL to check whether the window has a shape. |

## Return Value

Returns 0 if the window has a shape and, provided shape_mode was not NULL,
shape_mode has been filled with the mode data,
[SDL_NONSHAPEABLE_WINDOW](SDL_NONSHAPEABLE_WINDOW.md) if the
[SDL_Window](SDL_Window.md) given is not a shaped window, or
[SDL_WINDOW_LACKS_SHAPE](SDL_WINDOW_LACKS_SHAPE.md) if the
[SDL_Window](SDL_Window.md) given is a shapeable window currently lacking a
shape.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_WindowShapeMode](SDL_WindowShapeMode.md)
* [SDL_SetWindowShape](SDL_SetWindowShape.md)

----
[CategoryAPI](CategoryAPI.md)
