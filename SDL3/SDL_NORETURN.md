###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_NORETURN

A macro to tag a function as never-returning.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_NORETURN __attribute__((noreturn))
```

## Remarks

This is a hint to the compiler that a function does not return. An example
of a function like this is the C runtime's exit() function.

This hint can lead to code optimizations, and help analyzers understand
code flow better. On compilers without noreturn support, this is defined to
nothing.

This symbol is used in SDL's headers, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

