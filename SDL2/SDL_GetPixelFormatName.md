###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPixelFormatName

Get the human readable name of a pixel format.

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
const char* SDL_GetPixelFormatName(Uint32 format);
```

## Function Parameters

|        |            |                           |
| ------ | ---------- | ------------------------- |
| Uint32 | **format** | the pixel format to query |

## Return Value

(const char *) Returns the human readable name of the specified pixel
format or [`SDL_PIXELFORMAT_UNKNOWN`](SDL_PIXELFORMAT_UNKNOWN) if the
format isn't recognized.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPixels](CategoryPixels)

