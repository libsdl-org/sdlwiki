###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_EGL_ALLOW_TRANSPARENCY

A variable controlling whether the EGL window is allowed to be composited as transparent, rather than opaque.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_EGL_ALLOW_TRANSPARENCY "SDL_VIDEO_EGL_ALLOW_TRANSPARENCY"
```

## Remarks

Most window systems will always render windows opaque, even if the surface
format has an alpha channel. This is not always true, however, so by
default SDL will try to enforce opaque composition. To override this
behavior, you can set this hint to "1".

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

