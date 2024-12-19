###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDLCALL

A macro to set a function's calling conventions.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDLCALL __cdecl
```

## Remarks

SDL uses this macro for all its public functions, and any callbacks it
defines. This macro guarantees that calling conventions match between SDL
and the app, even if the two were built with different compilers or
optimization settings.

When writing a callback function, it is very important for it to be
correctly tagged with SDLCALL, as mismatched calling conventions can cause
strange behaviors and can be difficult to diagnose. Plus, on many
platforms, SDLCALL is defined to nothing, so compilers won't be able to
warn that the tag is missing.

This symbol is used in SDL's headers, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

