###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetSurfaceColorspace

Get the colorspace used by a surface.

## Syntax

```c
int SDL_GetSurfaceColorspace(SDL_Surface *surface, SDL_Colorspace *colorspace);

```

## Function Parameters

|                    |                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| **surface**        | the [SDL_Surface](SDL_Surface) structure to query                                                    |
| **colorspace**     | a pointer filled in with an [SDL_ColorSpace](SDL_ColorSpace) value describing the surface colorspace |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The colorspace defaults to [SDL_COLORSPACE_SCRGB](SDL_COLORSPACE_SCRGB) for
floating point formats, [SDL_COLORSPACE_HDR10](SDL_COLORSPACE_HDR10) for
10-bit formats, [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB) for other RGB
surfaces and [SDL_COLORSPACE_BT709_FULL](SDL_COLORSPACE_BT709_FULL) for YUV
textures.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

