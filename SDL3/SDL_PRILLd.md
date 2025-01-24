# SDL_PRILLd

A printf-formatting string for a `long long` value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRILLd SDL_PRILL_PREFIX "d"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRILLd " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

