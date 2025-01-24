# SDL_GetPixelFormatName

Get the human readable name of a pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
const char * SDL_GetPixelFormatName(SDL_PixelFormat format);
```

## Function Parameters

|                                    |            |                            |
| ---------------------------------- | ---------- | -------------------------- |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | the pixel format to query. |

## Return Value

(const char *) Returns the human readable name of the specified pixel
format or "[SDL_PIXELFORMAT_UNKNOWN](SDL_PIXELFORMAT_UNKNOWN)" if the
format isn't recognized.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

