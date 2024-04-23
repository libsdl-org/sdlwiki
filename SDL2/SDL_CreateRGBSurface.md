###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateRGBSurface

Allocate a new RGB surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
SDL_Surface* SDL_CreateRGBSurface
    (Uint32 flags, int width, int height, int depth,
     Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask);

```

## Function Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **flags**      | the flags are unused and should be set to 0 |
| **width**      | the width of the surface                    |
| **height**     | the height of the surface                   |
| **depth**      | the depth of the surface in bits            |
| **Rmask**      | the red mask for the pixels                 |
| **Gmask**      | the green mask for the pixels               |
| **Bmask**      | the blue mask for the pixels                |
| **Amask**      | the alpha mask for the pixels               |

## Return Value

Returns the new [SDL_Surface](SDL_Surface) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If `depth` is 4 or 8 bits, an empty palette is allocated for the surface.
If `depth` is greater than 8 bits, the pixel format is set using the
[RGBA]mask parameters.

The [RGBA]mask parameters are the bitmasks used to extract that color from
a pixel. For instance, `Rmask` being 0xFF000000 means the red data is
stored in the most significant byte. Using zeros for the RGB masks sets a
default value, based on the depth. For example:

```c++
SDL_CreateRGBSurface(0,w,h,32,0,0,0,0);
```

However, using zero for the Amask results in an Amask of 0.

By default surfaces with an alpha mask are set up for blending as with:

```c++
SDL_SetSurfaceBlendMode(surface, SDL_BLENDMODE_BLEND)
```

You can change this by calling
[SDL_SetSurfaceBlendMode](SDL_SetSurfaceBlendMode)() and selecting a
different `blendMode`.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRGBSurfaceFrom](SDL_CreateRGBSurfaceFrom)
* [SDL_CreateRGBSurfaceWithFormat](SDL_CreateRGBSurfaceWithFormat)
* [SDL_FreeSurface](SDL_FreeSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


