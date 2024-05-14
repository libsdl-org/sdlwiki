###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_KMSDRM_REQUIRE_DRM_MASTER

A variable that controls whether SDL requires DRM master access in order to initialize the KMSDRM video backend.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

The variable can be set to the following values:

- "0": SDL will allow usage of the KMSDRM backend without DRM master.
- "1": SDL Will require DRM master to use the KMSDRM backend. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

