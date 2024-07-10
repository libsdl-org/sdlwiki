###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertSurface

Copy an existing surface to a new surface of the specified format.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
SDL_Surface* SDL_ConvertSurface(SDL_Surface *surface, SDL_PixelFormat format);
```

## Function Parameters

|                                    |             |                                                               |
| ---------------------------------- | ----------- | ------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) *       | **surface** | the existing [SDL_Surface](SDL_Surface) structure to convert. |
| [SDL_PixelFormat](SDL_PixelFormat) | **format**  | the new pixel format.                                         |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns the new [SDL_Surface](SDL_Surface)
structure that is created or NULL if it fails; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function is used to optimize images for faster *repeat* blitting. This
is accomplished by converting the original and storing the result as a new
surface. The new, optimized surface can then be used as the source for
future blits, making them faster.

If you are converting to an indexed surface and want to map colors to a
palette, you can use
[SDL_ConvertSurfaceAndColorspace](SDL_ConvertSurfaceAndColorspace)()
instead.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c

SDL_Surface *input;

SDL_PixelFormat *format = SDL_CreatePixelFormat(SDL_PIXELFORMAT_RGBA32);
SDL_Surface *output = SDL_ConvertSurface(input, format);
SDL_DestroyPixelFormat(format);

```

## See Also

- [SDL_ConvertSurfaceAndColorspace](SDL_ConvertSurfaceAndColorspace)
- [SDL_DestroySurface](SDL_DestroySurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

