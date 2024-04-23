###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_DIRECT3D_THREADSAFE

A variable controlling whether the Direct3D device is initialized for thread-safe operations.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_DIRECT3D_THREADSAFE "SDL_RENDER_DIRECT3D_THREADSAFE"
```

## Remarks

This variable can be set to the following values:

- "0": Thread-safety is not enabled (faster)
- "1": Thread-safety is enabled

By default the Direct3D device is created with thread-safety disabled.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)



