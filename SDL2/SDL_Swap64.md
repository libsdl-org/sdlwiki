# SDL_Swap64

Use this function to swap the byte order of a 64-bit value.

## Header File

Defined in [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_endian.h)

## Syntax

```c
SDL_FORCE_INLINE Uint64 SDL_Swap64(Uint64 x);
```

## Function Parameters

|                  |       |                          |
| ---------------- | ----- | ------------------------ |
| [Uint64](Uint64) | **x** | the value to be swapped. |

## Return Value

([Uint64](Uint64)) Returns the swapped value.

## See Also

- [SDL_SwapBE64](SDL_SwapBE64)
- [SDL_SwapLE64](SDL_SwapLE64)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEndian](CategoryEndian)

