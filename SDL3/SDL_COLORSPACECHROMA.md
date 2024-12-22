###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_COLORSPACECHROMA

A macro to retrieve the chroma sample location of an [SDL_Colorspace](SDL_Colorspace).

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_COLORSPACECHROMA(cspace)     (SDL_ChromaLocation)(((cspace) >> 20) & 0x0F)
```

## Macro Parameters

|            |                                               |
| ---------- | --------------------------------------------- |
| **cspace** | an [SDL_Colorspace](SDL_Colorspace) to check. |

## Return Value

Returns the [SDL_ChromaLocation](SDL_ChromaLocation) of `cspace`.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

