# SDL_ALLOC_SIZE

A macro to tag a function as returning a certain allocation.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_ALLOC_SIZE(p) __attribute__((alloc_size(p)))
```

## Remarks

This is a hint to the compiler that a function allocates and returns a
specific amount of memory based on one of its arguments. For example, the C
runtime's malloc() function could use this macro with an argument of 1
(first argument to malloc is the size of the allocation).

On compilers without alloc_size support, this is defined to nothing.

Most apps don't need to, and should not, use this directly.

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

