###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Swap16BE

Swap a 16-bit value from bigendian to native byte order.

## Header File

Defined in [<SDL3/SDL_endian.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_endian.h)

## Syntax

```c
#define SDL_Swap16BE(x) SwapOnlyIfNecessary(x)
```

## Macro Parameters

|       |                                             |
| ----- | ------------------------------------------- |
| **x** | the value to swap, in bigendian byte order. |

## Return Value

Returns `x` in native byte order.

## Remarks

If this is running on a bigendian system, `x` is returned unchanged.

This macro never references `x` more than once, avoiding side effects.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryEndian](CategoryEndian)

