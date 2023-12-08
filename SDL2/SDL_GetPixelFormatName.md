###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPixelFormatName

Get the human readable name of a pixel format.

## Syntax

```c
const char* SDL_GetPixelFormatName(Uint32 format);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **format**     | the pixel format to query |

## Return Value

Returns the human readable name of the specified pixel format or
[`SDL_PIXELFORMAT_UNKNOWN`](SDL_PIXELFORMAT_UNKNOWN) if the format isn't
recognized.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
