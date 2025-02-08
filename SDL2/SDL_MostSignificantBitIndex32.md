# SDL_MostSignificantBitIndex32

Use this function to get the index of the most significant (set) bit in a

## Header File

Defined in [SDL_bits.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_bits.h)

## Syntax

```c
SDL_FORCE_INLINE int SDL_MostSignificantBitIndex32(Uint32 x);
```

## Function Parameters

|                  |       |                                |
| ---------------- | ----- | ------------------------------ |
| [Uint32](Uint32) | **x** | the number to find the MSB of. |

## Return Value

(int) Returns the index of the most significant bit of x, or -1 if x is 0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryBits](CategoryBits)

