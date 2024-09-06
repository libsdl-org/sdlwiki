###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MIN_SINT32

The smallest value that can be held in a signed 32-bit integer.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_MIN_SINT32  ((Sint32)(~0x7FFFFFFF)) /* -2147483648 */
```

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

