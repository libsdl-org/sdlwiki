# SDL_Swap16

Use this function to swap the byte order of a 16-bit value.

## Header File

Defined in [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_endian.h)

## Syntax

```c
SDL_FORCE_INLINE Uint16 SDL_Swap16(Uint16 x);
```

## Function Parameters

|                  |       |                          |
| ---------------- | ----- | ------------------------ |
| [Uint16](Uint16) | **x** | the value to be swapped. |

## Return Value

([Uint16](Uint16)) Returns the swapped value.

## See Also

- [SDL_SwapBE16](SDL_SwapBE16)
- [SDL_SwapLE16](SDL_SwapLE16)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEndian](CategoryEndian)

