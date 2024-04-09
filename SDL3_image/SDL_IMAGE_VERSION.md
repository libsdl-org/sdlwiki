###### (This function is part of SDL_image, a separate library from SDL.)
# SDL_IMAGE_VERSION

This macro can be used to fill a version structure with the compile-time version of the SDL_image library.

## Header File

Defined in SDL_image.h

## Syntax

```c
#define SDL_IMAGE_VERSION(X)                        \
{                                                   \
    (X)->major = SDL_IMAGE_MAJOR_VERSION;           \
    (X)->minor = SDL_IMAGE_MINOR_VERSION;           \
    (X)->patch = SDL_IMAGE_PATCHLEVEL;              \
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

