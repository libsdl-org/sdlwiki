###### (This function is part of SDL_mixer, a separate library from SDL.)
# SDL_MIXER_COMPILEDVERSION

This is the version number macro for the current SDL_mixer version.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
#define SDL_MIXER_COMPILEDVERSION \
    SDL_VERSIONNUM(SDL_MIXER_MAJOR_VERSION, SDL_MIXER_MINOR_VERSION, SDL_MIXER_PATCHLEVEL)
```

## Remarks

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300. This macro will
not be available in SDL 3.x or SDL_mixer 3.x.

Deprecated, use SDL_MIXER_VERSION_ATLEAST or SDL_MIXER_VERSION instead.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

