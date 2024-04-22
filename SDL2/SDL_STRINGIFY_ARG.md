###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_STRINGIFY_ARG

Macro useful for building other macros with strings in them

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
#define SDL_STRINGIFY_ARG(arg)  #arg
```

## Remarks

e.g. #define LOG_ERROR(X)
OutputDebugString([SDL_STRINGIFY_ARG](SDL_STRINGIFY_ARG)(__FUNCTION__) ": "
X "\n")

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

