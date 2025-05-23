# SDL_Swap32

Byte-swap an unsigned 32-bit number.

## Header File

Defined in [<SDL3/SDL_endian.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_endian.h)

## Syntax

```c
SDL_FORCE_INLINE Uint32 SDL_Swap32(Uint32 x);
```

## Function Parameters

|                  |       |                         |
| ---------------- | ----- | ----------------------- |
| [Uint32](Uint32) | **x** | the value to byte-swap. |

## Return Value

([Uint32](Uint32)) Returns `x`, with its bytes in the opposite endian
order.

## Remarks

This will always byte-swap the value, whether it's currently in the native
byteorder of the system or not. You should use [SDL_Swap32LE](SDL_Swap32LE)
or [SDL_Swap32BE](SDL_Swap32BE) instead, in most cases.

Note that this is a forced-inline function in a header, and not a public
API function available in the SDL library (which is to say, the code is
embedded in the calling program and the linker and dynamic loader will not
be able to find this function inside SDL itself).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEndian](CategoryEndian)

