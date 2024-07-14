###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SINT64_C

Append the 64 bit integer suffix to a signed integer literal.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_SINT64_C(c)  c ## LL  /* or whatever the current compiler uses. */
```

## Remarks

This helps compilers that might believe a integer literal larger than
0xFFFFFFFF is overflowing a 32-bit value. Use `SDL_SINT64_C(0xFFFFFFFF1)`
instead of `0xFFFFFFFF1` by itself.

## Version

This macro is available since SDL 3.0.0.

## See Also

- [SDL_UINT64_C](SDL_UINT64_C)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

