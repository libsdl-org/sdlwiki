###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_isinf

Return whether the value is infinity.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_isinf(double x);
```

## Function Parameters

|        |       |                                        |
| ------ | ----- | -------------------------------------- |
| double | **x** | double-precision floating point value. |

## Return Value

(int) Returns non-zero if the value is infinity, 0 otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_isinff](SDL_isinff)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

