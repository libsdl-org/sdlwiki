###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMasksForPixelFormat

Convert one of the enumerated pixel formats to a bpp value and RGBA masks.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
int SDL_GetMasksForPixelFormat(SDL_PixelFormat format, int *bpp, Uint32 *Rmask, Uint32 *Gmask, Uint32 *Bmask, Uint32 *Amask);
```

## Function Parameters

|                                    |            |                                                         |
| ---------------------------------- | ---------- | ------------------------------------------------------- |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | one of the [SDL_PixelFormat](SDL_PixelFormat) values.   |
| int *                              | **bpp**    | a bits per pixel value; usually 15, 16, or 32.          |
| Uint32 *                           | **Rmask**  | a pointer filled in with the red mask for the format.   |
| Uint32 *                           | **Gmask**  | a pointer filled in with the green mask for the format. |
| Uint32 *                           | **Bmask**  | a pointer filled in with the blue mask for the format.  |
| Uint32 *                           | **Amask**  | a pointer filled in with the alpha mask for the format. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPixelFormatForMasks](SDL_GetPixelFormatForMasks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

