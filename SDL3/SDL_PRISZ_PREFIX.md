# SDL_PRISZ_PREFIX

A printf-formatting string prefix for a `size_t` value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRISZ_PREFIX "z"
```

## Remarks

This is just the prefix! You probably actually want
[SDL_PRISZu](SDL_PRISZu), [SDL_PRISZx](SDL_PRISZx), or
[SDL_PRISZX](SDL_PRISZX) instead.

Use it like this:

```c
SDL_Log("There are %" SDL_PRISZ_PREFIX "u bottles of beer on the wall.", bottles);
```

## Version

This macro is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

