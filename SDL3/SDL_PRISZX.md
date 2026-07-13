# SDL_PRISZX

A printf-formatting string for an `size_t` value as upper-case hexadecimal.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRISZX SDL_PRISZ_PREFIX "X"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRISZX " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

