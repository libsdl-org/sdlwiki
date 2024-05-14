###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_DIRECT3D11_DEBUG

A variable controlling whether to enable Direct3D 11+'s Debug Layer.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_DIRECT3D11_DEBUG    "SDL_RENDER_DIRECT3D11_DEBUG"
```

## Remarks

This variable does not have any effect on the Direct3D 9 based renderer.

This variable can be set to the following values:

- "0": Disable Debug Layer use
- "1": Enable Debug Layer use

By default, SDL does not use Direct3D Debug Layer.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

