###### (This function is part of SDL_image, a separate library from SDL.)
# SDL_IMAGE_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_image at least X.Y.Z.

## Header File

Defined in SDL_image.h

## Syntax

```c
#define SDL_IMAGE_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_IMAGE_MAJOR_VERSION >= X) && \
     (SDL_IMAGE_MAJOR_VERSION > X || SDL_IMAGE_MINOR_VERSION >= Y) && \
     (SDL_IMAGE_MAJOR_VERSION > X || SDL_IMAGE_MINOR_VERSION > Y || SDL_IMAGE_PATCHLEVEL >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

