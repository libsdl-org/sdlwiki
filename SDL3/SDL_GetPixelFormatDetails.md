###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPixelFormatDetails

Create an [SDL_PixelFormatDetails](SDL_PixelFormatDetails) structure corresponding to a pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
const SDL_PixelFormatDetails * SDL_GetPixelFormatDetails(SDL_PixelFormat format);
```

## Function Parameters

|                                    |            |                                                       |
| ---------------------------------- | ---------- | ----------------------------------------------------- |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | one of the [SDL_PixelFormat](SDL_PixelFormat) values. |

## Return Value

(const [SDL_PixelFormatDetails](SDL_PixelFormatDetails) *) Returns a
pointer to a [SDL_PixelFormatDetails](SDL_PixelFormatDetails) structure or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Returned structure may come from a shared global cache (i.e. not newly
allocated), and hence should not be modified, especially the palette. Weird
errors such as `Blit combination not supported` may occur.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

