###### (This function is part of SDL_mixer, a separate library from SDL.)
# SDL_MIXER_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_mixer at least X.Y.Z.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
#define SDL_MIXER_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_MIXER_MAJOR_VERSION >= X) && \
     (SDL_MIXER_MAJOR_VERSION > X || SDL_MIXER_MINOR_VERSION >= Y) && \
     (SDL_MIXER_MAJOR_VERSION > X || SDL_MIXER_MINOR_VERSION > Y || SDL_MIXER_MICRO_VERSION >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

