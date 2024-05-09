###### (This function is part of SDL_mixer, a separate library from SDL.)
# SDL_MIXER_VERSION

This macro can be used to fill a version structure with the compile-time version of the SDL_mixer library.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
#define SDL_MIXER_VERSION(X)                        \
{                                                   \
    (X)->major = SDL_MIXER_MAJOR_VERSION;           \
    (X)->minor = SDL_MIXER_MINOR_VERSION;           \
    (X)->patch = SDL_MIXER_PATCHLEVEL;              \
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

