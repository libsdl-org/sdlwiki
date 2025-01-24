# SDL_PRILL_PREFIX

A printf-formatting string prefix for a `long long` value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRILL_PREFIX "ll"
```

## Remarks

This is just the prefix! You probably actually want
[SDL_PRILLd](SDL_PRILLd), [SDL_PRILLu](SDL_PRILLu),
[SDL_PRILLx](SDL_PRILLx), or [SDL_PRILLX](SDL_PRILLX) instead.

Use it like this:

```c
SDL_Log("There are %" SDL_PRILL_PREFIX "d bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

