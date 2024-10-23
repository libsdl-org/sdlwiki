###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# Sint64

A signed 64-bit integer type.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef int64_t Sint64;
#define SDL_MAX_SINT64  SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)   /* 9223372036854775807 */
#define SDL_MIN_SINT64  ~SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)  /* -9223372036854775808 */
```

## Version

This macro is available since SDL 3.1.3.

## See Also

- [SDL_SINT64_C](SDL_SINT64_C)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

