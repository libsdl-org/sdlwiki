###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowShape

Set the shape of a transparent window.

## Syntax

```c
int SDL_SetWindowShape(SDL_Window *window, SDL_Surface *shape);

```

## Function Parameters

|                |                                                                                       |
| -------------- | ------------------------------------------------------------------------------------- |
| **window**     | the window                                                                            |
| **shape**      | the surface representing the shape of the window, or NULL to remove any current shape |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This sets the alpha channel of a transparent window and any fully
transparent areas are also transparent to mouse clicks. If you are using
something besides the SDL render API, then you are responsible for setting
the alpha channel of the window yourself.

The shape is copied inside this function, so you can free it afterwards. If
your shape surface changes, you should call
[SDL_SetWindowShape](SDL_SetWindowShape)() again to update the window.

The window must have been created with the
[SDL_WINDOW_TRANSPARENT](SDL_WINDOW_TRANSPARENT) flag.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

