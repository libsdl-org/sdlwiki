###### (This function is part of SDL_ttf, a separate library from SDL.)
# SDL_TTF_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_ttf at least X.Y.Z.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
#define SDL_TTF_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_TTF_MAJOR_VERSION >= X) && \
     (SDL_TTF_MAJOR_VERSION > X || SDL_TTF_MINOR_VERSION >= Y) && \
     (SDL_TTF_MAJOR_VERSION > X || SDL_TTF_MINOR_VERSION > Y || SDL_TTF_PATCHLEVEL >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

