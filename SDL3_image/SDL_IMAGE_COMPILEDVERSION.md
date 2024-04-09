###### (This function is part of SDL_image, a separate library from SDL.)
# SDL_IMAGE_COMPILEDVERSION

This is the version number macro for the current SDL_image version.

## Header File

Defined in SDL_image.h

## Syntax

```c
#define SDL_IMAGE_COMPILEDVERSION \
    SDL_VERSIONNUM(SDL_IMAGE_MAJOR_VERSION, SDL_IMAGE_MINOR_VERSION, SDL_IMAGE_PATCHLEVEL)
```

## Remarks

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300. This macro will
not be available in SDL 3.x or SDL_image 3.x.

Deprecated, use SDL_IMAGE_VERSION_ATLEAST or SDL_IMAGE_VERSION instead.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

