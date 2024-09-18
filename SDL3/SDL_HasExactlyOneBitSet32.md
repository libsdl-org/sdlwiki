###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasExactlyOneBitSet32

Determine if a unsigned 32-bit value has exactly one bit set.

## Header File

Defined in [<SDL3/SDL_bits.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_bits.h)

## Syntax

```c
SDL_FORCE_INLINE bool SDL_HasExactlyOneBitSet32(Uint32 x);
```

## Function Parameters

|        |       |                              |
| ------ | ----- | ---------------------------- |
| Uint32 | **x** | the 32-bit value to examine. |

## Return Value

(bool) Returns true if exactly one bit is set in `x`, false otherwise.

## Remarks

If there are no bits set (`x` is zero), or more than one bit set, this
returns false. If any one bit is exclusively set, this returns true.

Note that this is a forced-inline function in a header, and not a public
API function available in the SDL library (which is to say, the code is
embedded in the calling program and the linker and dynamic loader will not
be able to find this function inside SDL itself).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryBits](CategoryBits)

