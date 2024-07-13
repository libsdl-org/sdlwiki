###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateSurfacePalette

Create a palette and associate it with a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Palette * SDL_CreateSurfacePalette(SDL_Surface *surface);
```

## Function Parameters

|                              |             |                                                     |
| ---------------------------- | ----------- | --------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update. |

## Return Value

([SDL_Palette](SDL_Palette) *) Returns a new [SDL_Palette](SDL_Palette)
structure on success or NULL on failure (e.g. if the surface didn't have an
index format); call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function creates a palette compatible with the provided surface. The
palette is then returned for you to modify, and the surface will
automatically use the new palette in future operations. You do not need to
destroy the returned palette, it will be freed when the reference count
reaches 0, usually when the surface is destroyed.

Bitmap surfaces (with format
[SDL_PIXELFORMAT_INDEX1LSB](SDL_PIXELFORMAT_INDEX1LSB) or
[SDL_PIXELFORMAT_INDEX1MSB](SDL_PIXELFORMAT_INDEX1MSB)) will have the
palette initialized with 0 as white and 1 as black. Other surfaces will get
a palette initialized with white in every entry.

If this function is called for a surface that already has a palette, a new
palette will be created to replace it.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetPaletteColors](SDL_SetPaletteColors)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

