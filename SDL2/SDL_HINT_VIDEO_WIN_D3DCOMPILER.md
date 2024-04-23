###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_WIN_D3DCOMPILER

A variable specifying which shader compiler to preload when using the Chrome ANGLE binaries

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WIN_D3DCOMPILER              "SDL_VIDEO_WIN_D3DCOMPILER"
```

## Remarks

SDL has EGL and OpenGL ES2 support on Windows via the ANGLE project. It can
use two different sets of binaries, those compiled by the user from source
or those provided by the Chrome browser. In the later case, these binaries
require that SDL loads a DLL providing the shader compiler.

This variable can be set to the following values:

- "d3dcompiler_46.dll: default, best for Vista or later.
- "d3dcompiler_43.dll: for XP support.
- "none": do not load any library, useful if you compiled ANGLE from source
  and included the compiler in your binaries.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)



