# SDL_SetSurfacePalette

Set the palette used by a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SetSurfacePalette(SDL_Surface *surface, SDL_Palette *palette);
```

## Function Parameters

|                              |             |                                                     |
| ---------------------------- | ----------- | --------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to update. |
| [SDL_Palette](SDL_Palette) * | **palette** | the [SDL_Palette](SDL_Palette) structure to use.    |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Setting the palette keeps an internal reference to the palette, which can
be safely destroyed afterwards.

A single palette can be shared with many surfaces.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreatePalette](SDL_CreatePalette)
- [SDL_GetSurfacePalette](SDL_GetSurfacePalette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

