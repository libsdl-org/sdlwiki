###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

Return 0 on success,
[SDL_INVALID_SHAPE_ARGUMENT](SDL_INVALID_SHAPE_ARGUMENT.md) on an invalid
shape argument, or [SDL_NONSHAPEABLE_WINDOW](SDL_NONSHAPEABLE_WINDOW.md) if
the [SDL_Window](SDL_Window.md) given does not reference a valid shaped
window.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_WindowShapeMode](SDL_WindowShapeMode.md)
* [SDL_GetShapedWindowMode](SDL_GetShapedWindowMode.md)

----
[CategoryAPI](CategoryAPI.md)
