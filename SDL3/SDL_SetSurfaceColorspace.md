###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetSurfaceColorspace

Set the colorspace used by a surface.

## Syntax

```c
int SDL_SetSurfaceColorspace(SDL_Surface *surface, SDL_Colorspace colorspace);

```

## Function Parameters

|                    |                                                                             |
| ------------------ | --------------------------------------------------------------------------- |
| **surface**        | the [SDL_Surface](SDL_Surface) structure to update                          |
| **colorspace**     | an [SDL_ColorSpace](SDL_ColorSpace) value describing the surface colorspace |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Setting the colorspace doesn't change the pixels, only how they are
interpreted in color operations.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

