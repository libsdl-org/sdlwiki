# SDL_PRILLX

A printf-formatting string for an `unsigned long long` value as upper-case hexadecimal.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRILLX SDL_PRILL_PREFIX "X"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRILLX " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

