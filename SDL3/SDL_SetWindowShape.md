###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowShape

Set the shape and parameters of a shaped window.

## Syntax

```c
int SDL_SetWindowShape(SDL_Window *window,SDL_Surface *shape,SDL_WindowShapeMode *shape_mode);

```

## Function Parameters

|                    |                                                      |
| ------------------ | ---------------------------------------------------- |
| **window**         | The shaped window whose parameters should be set.    |
| **shape**          | A surface encoding the desired shape for the window. |
| **shape_mode**     | The parameters to set for the shaped window.         |

## Return Value

Returns 0 on success,
[SDL_INVALID_SHAPE_ARGUMENT](SDL_INVALID_SHAPE_ARGUMENT) on an invalid
shape argument, or [SDL_NONSHAPEABLE_WINDOW](SDL_NONSHAPEABLE_WINDOW) if
the [SDL_Window](SDL_Window) given does not reference a valid shaped
window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_WindowShapeMode](SDL_WindowShapeMode)
* [SDL_GetShapedWindowMode](SDL_GetShapedWindowMode)

----
[CategoryAPI](CategoryAPI)

