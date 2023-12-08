###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertSurface

Copy an existing surface to a new surface of the specified format.

## Syntax

```c
SDL_Surface* SDL_ConvertSurface(SDL_Surface *surface,
                                const SDL_PixelFormat *format);

```

## Function Parameters

|                 |                                                                                        |
| --------------- | -------------------------------------------------------------------------------------- |
| **surface**     | the existing [SDL_Surface](SDL_Surface.md) structure to convert                           |
| **format**      | the [SDL_PixelFormat](SDL_PixelFormat.md) structure that the new surface is optimized for |

## Return Value

Returns the new [SDL_Surface](SDL_Surface.md) structure that is created or
NULL if it fails; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function is used to optimize images for faster *repeat* blitting. This
is accomplished by converting the original and storing the result as a new
surface. The new, optimized surface can then be used as the source for
future blits, making them faster.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++

// SDL_Surface *input = ...;
SDL_PixelFormat *format = SDL_CreatePixelFormat(SDL_PIXELFORMAT_RGBA32);
SDL_Surface *output = SDL_ConvertSurface(input, format, 0);
SDL_DestroyPixelFormat(format);

```

## Related Functions

* [SDL_CreatePixelFormat](SDL_CreatePixelFormat.md)
* [SDL_ConvertSurfaceFormat](SDL_ConvertSurfaceFormat.md)
* [SDL_CreateSurface](SDL_CreateSurface.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySurface](CategorySurface.md)
