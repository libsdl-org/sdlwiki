###### (This function is part of SDL_ttf, a separate library from SDL.)
# SDL_TTF_VERSION

This macro can be used to fill a version structure with the compile-time version of the SDL_ttf library.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
#define SDL_TTF_VERSION(X)                          \
{                                                   \
    (X)->major = SDL_TTF_MAJOR_VERSION;             \
    (X)->minor = SDL_TTF_MINOR_VERSION;             \
    (X)->patch = SDL_TTF_PATCHLEVEL;                \
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

