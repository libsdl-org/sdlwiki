###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_KMSDRM_REQUIRE_DRM_MASTER

Determines whether SDL enforces that DRM master is required in order to initialize the KMSDRM video backend.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_KMSDRM_REQUIRE_DRM_MASTER      "SDL_KMSDRM_REQUIRE_DRM_MASTER"
```

## Remarks

The DRM subsystem has a concept of a "DRM master" which is a DRM client
that has the ability to set planes, set cursor, etc. When SDL is DRM
master, it can draw to the screen using the SDL rendering APIs. Without DRM
master, SDL is still able to process input and query attributes of attached
displays, but it cannot change display state or draw to the screen
directly.

In some cases, it can be useful to have the KMSDRM backend even if it
cannot be used for rendering. An app may want to use SDL for input
processing while using another rendering API (such as an MMAL overlay on
Raspberry Pi) or using its own code to render to DRM overlays that SDL
doesn't support.

This hint must be set before initializing the video subsystem.

This variable can be set to the following values:

- "0": SDL will allow usage of the KMSDRM backend without DRM master
- "1": SDL Will require DRM master to use the KMSDRM backend (default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

