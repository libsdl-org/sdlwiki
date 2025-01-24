# SDL_HINT_EGL_LIBRARY

Specify the EGL library to load.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EGL_LIBRARY "SDL_EGL_LIBRARY"
```

## Remarks

This hint should be set before creating an OpenGL window or creating an
OpenGL context. This hint is only considered if SDL is using EGL to manage
OpenGL contexts. If this hint isn't set, SDL will choose a reasonable
default.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

