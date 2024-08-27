###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PremultiplySurfaceAlpha

Premultiply the alpha in a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_bool SDL_PremultiplySurfaceAlpha(SDL_Surface *surface, SDL_bool linear);
```

## Function Parameters

|                              |             |                                                                                                                                                    |
| ---------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the surface to modify.                                                                                                                             |
| [SDL_bool](SDL_bool)         | **linear**  | [SDL_TRUE](SDL_TRUE) to convert from sRGB to linear space for the alpha multiplication, [SDL_FALSE](SDL_FALSE) to do multiplication in sRGB space. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This is safe to use with src == dst, but not for other overlapping areas.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

