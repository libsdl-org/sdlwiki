###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_VITA_PVR_OPENGL

A variable controlling whether OpenGL should be used instead of OpenGL ES on the PlayStation Vita.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VITA_PVR_OPENGL "SDL_VITA_PVR_OPENGL"
```

## Remarks

The variable can be set to the following values:

- "0": Use OpenGL ES. (default)
- "1": Use OpenGL.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

