# SDL_PRIs64

A printf-formatting string for an [Sint64](Sint64) value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRIs64 "lld"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRIs64 " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

