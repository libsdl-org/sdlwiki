###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PremultiplySurfaceAlpha

Premultiply the alpha in a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_PremultiplySurfaceAlpha(SDL_Surface *surface, bool linear);
```

## Function Parameters

|                              |             |                                                                                                                   |
| ---------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to modify.                                                                                            |
| bool                         | **linear**  | true to convert from sRGB to linear space for the alpha multiplication, false to do multiplication in sRGB space. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is safe to use with src == dst, but not for other overlapping areas.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

