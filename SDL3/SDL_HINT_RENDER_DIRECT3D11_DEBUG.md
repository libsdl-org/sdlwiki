###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_RENDER_DIRECT3D11_DEBUG

A variable controlling whether to enable Direct3D 11+'s Debug Layer.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_RENDER_DIRECT3D11_DEBUG    "SDL_RENDER_DIRECT3D11_DEBUG"
```

## Remarks

This variable does not have any effect on the Direct3D 9 based renderer.

The variable can be set to the following values:

- "0": Disable Debug Layer use. (default)
- "1": Enable Debug Layer use.

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


