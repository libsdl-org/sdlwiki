###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_FRAMEBUFFER_ACCELERATION

A variable controlling how 3D acceleration is used to accelerate the SDL screen surface.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_FRAMEBUFFER_ACCELERATION   "SDL_FRAMEBUFFER_ACCELERATION"
```

## Remarks

SDL can try to accelerate the SDL screen surface by using streaming
textures with a 3D rendering engine. This variable controls whether and how
this is done.

This variable can be set to the following values:

- "0": Disable 3D acceleration
- "1": Enable 3D acceleration, using the default renderer.
- "X": Enable 3D acceleration, using X where X is one of the valid
  rendering drivers. (e.g. "direct3d", "opengl", etc.)

By default SDL tries to make a best guess for each platform whether to use
acceleration or not.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

