###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Unsupported

A macro to standardize error reporting on unsupported operations.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
#define SDL_Unsupported()               SDL_SetError("That operation is not supported")
```

## Remarks

This simply calls [SDL_SetError](SDL_SetError)() with a standardized error
string, for convenience, consistency, and clarity.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryError](CategoryError)

