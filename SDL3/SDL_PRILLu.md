# SDL_PRILLu

A printf-formatting string for a `unsigned long long` value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRILLu SDL_PRILL_PREFIX "u"
```

## Remarks

Use it like this:

```c
SDL_Log("There are %" SDL_PRILLu " bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

