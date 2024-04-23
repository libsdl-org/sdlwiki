###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AllocFormat

Create an [SDL_PixelFormat](SDL_PixelFormat) structure corresponding to a pixel format.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
SDL_PixelFormat * SDL_AllocFormat(Uint32 pixel_format);

```

## Function Parameters

|                      |                                                              |
| -------------------- | ------------------------------------------------------------ |
| **pixel_format**     | one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values |

## Return Value

Returns the new [SDL_PixelFormat](SDL_PixelFormat) structure or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Returned structure may come from a shared global cache (i.e. not newly
allocated), and hence should not be modified, especially the palette. Weird
errors such as `Blit combination not supported` may occur.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_FreeFormat](SDL_FreeFormat)


## Example

```c
SDL_PixelFormat* pixel_format = NULL;

/* ... */

SDL_Init(SDL_INIT_EVERYTHING);

pixel_format = SDL_AllocFormat(SDL_PIXELFORMAT_RGBA32);

if (pixel_format == NULL) printf( "Error: %s\n", SDL_GetError() );

/* ... */

printf("Amount of bytes: %i\n", pixel_format->BytesPerPixel);

```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

