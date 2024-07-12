###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPixelFormatName

Get the human readable name of a pixel format.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
const char* SDL_GetPixelFormatName(SDL_PixelFormat format);
```

## Function Parameters

|                                    |            |                            |
| ---------------------------------- | ---------- | -------------------------- |
| [SDL_PixelFormat](SDL_PixelFormat) | **format** | the pixel format to query. |

## Return Value

(const char *) Returns the human readable name of the specified pixel
format or [`SDL_PIXELFORMAT_UNKNOWN`](SDL_PIXELFORMAT_UNKNOWN) if the
format isn't recognized.

## Remarks

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_Surface* surface; // a valid surface from wherever.
const char* surfacePixelFormatName = SDL_GetPixelFormatName(surface->format);
SDL_Log("The surface's pixelformat is %s", surfacePixelFormatName);
// prints something like "The surface's pixelformat is SDL_PIXELFORMAT_ABGR8888"
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

