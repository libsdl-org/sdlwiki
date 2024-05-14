###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_FRAMEBUFFER_ACCELERATION

A variable controlling how 3D acceleration is used to accelerate the SDL screen surface.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_FRAMEBUFFER_ACCELERATION   "SDL_FRAMEBUFFER_ACCELERATION"
```

## Remarks

SDL can try to accelerate the SDL screen surface by using streaming
textures with a 3D rendering engine. This variable controls whether and how
this is done.

The variable can be set to the following values:

- "0": Disable 3D acceleration
- "1": Enable 3D acceleration, using the default renderer. (default)
- "X": Enable 3D acceleration, using X where X is one of the valid
  rendering drivers. (e.g. "direct3d", "opengl", etc.)

This hint should be set before calling
[SDL_GetWindowSurface](SDL_GetWindowSurface)()

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

