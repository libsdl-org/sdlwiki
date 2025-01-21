###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DECLSPEC

A macro to tag a symbol as a public API.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_DECLSPEC __attribute__ ((visibility("default")))
```

## Remarks

SDL uses this macro for all its public functions. On some targets, it is
used to signal to the compiler that this function needs to be exported from
a shared library, but it might have other side effects.

This symbol is used in SDL's headers, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

