# SDLMAIN_DECLSPEC

A macro to tag a main entry point function as exported.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
#define SDLMAIN_DECLSPEC
```

## Remarks

Most platforms don't need this, and the macro will be defined to nothing.
Some, like Android, keep the entry points in a shared library and need to
explicitly export the symbols.

External code rarely needs this, and if it needs something, it's almost
always [SDL_DECLSPEC](SDL_DECLSPEC) instead.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_DECLSPEC](SDL_DECLSPEC)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMain](CategoryMain)

