# SDL_FORCE_INLINE

A macro to demand a function be inlined.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_FORCE_INLINE __forceinline
```

## Remarks

This is a command to the compiler to inline a function. SDL uses this macro
in its public headers for a handful of simple functions. On compilers
without forceinline support, this is defined to `static SDL_INLINE`, which
is often good enough.

This symbol is used in SDL's headers, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

