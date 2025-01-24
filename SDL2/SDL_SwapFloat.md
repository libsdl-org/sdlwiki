# SDL_SwapFloat

Use this function to swap the byte order of a floating point value.

## Header File

Defined in [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_endian.h)

## Syntax

```c
SDL_FORCE_INLINE float SDL_SwapFloat(float x);
```

## Function Parameters

|       |       |                          |
| ----- | ----- | ------------------------ |
| float | **x** | the value to be swapped. |

## Return Value

(float) Returns the swapped value.

## See Also

- [SDL_SwapFloatBE](SDL_SwapFloatBE)
- [SDL_SwapFloatLE](SDL_SwapFloatLE)


## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEndian](CategoryEndian)

