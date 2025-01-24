# SDL_Swap32

Use this function to swap the byte order of a 32-bit value.

## Header File

Defined in [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_endian.h)

## Syntax

```c
SDL_FORCE_INLINE Uint32 SDL_Swap32(Uint32 x);
```

## Function Parameters

|                  |       |                          |
| ---------------- | ----- | ------------------------ |
| [Uint32](Uint32) | **x** | the value to be swapped. |

## Return Value

([Uint32](Uint32)) Returns the swapped value.

## See Also

- [SDL_SwapBE32](SDL_SwapBE32)
- [SDL_SwapLE32](SDL_SwapLE32)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEndian](CategoryEndian)

