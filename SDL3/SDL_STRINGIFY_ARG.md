###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_STRINGIFY_ARG

Macro useful for building other macros with strings in them.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_STRINGIFY_ARG(arg)  #arg
```

## Remarks

For example:

```c
#define LOG_ERROR(X) OutputDebugString(SDL_STRINGIFY_ARG(__FUNCTION__) ": " X "\n")`
```

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

