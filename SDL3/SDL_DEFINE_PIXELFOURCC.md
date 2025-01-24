# SDL_DEFINE_PIXELFOURCC

A macro for defining custom FourCC pixel formats.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_DEFINE_PIXELFOURCC(A, B, C, D) SDL_FOURCC(A, B, C, D)
```

## Macro Parameters

|       |                                          |
| ----- | ---------------------------------------- |
| **A** | the first character of the FourCC code.  |
| **B** | the second character of the FourCC code. |
| **C** | the third character of the FourCC code.  |
| **D** | the fourth character of the FourCC code. |

## Return Value

Returns a format value in the style of [SDL_PixelFormat](SDL_PixelFormat).

## Remarks

For example, defining [SDL_PIXELFORMAT_YV12](SDL_PIXELFORMAT_YV12) looks
like this:

```c
SDL_DEFINE_PIXELFOURCC('Y', 'V', '1', '2')
```

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

