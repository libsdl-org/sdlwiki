###### (This function is part of SDL_ttf, a separate library from SDL.)
# SDL_TTF_COMPILEDVERSION

This is the version number macro for the current SDL_ttf version.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
#define SDL_TTF_COMPILEDVERSION \
    SDL_VERSIONNUM(SDL_TTF_MAJOR_VERSION, SDL_TTF_MINOR_VERSION, SDL_TTF_PATCHLEVEL)
```

## Remarks

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300. This macro will
not be available in SDL 3.x or SDL_ttf 3.x.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

