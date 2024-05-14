###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WIN_D3DCOMPILER

A variable specifying which shader compiler to preload when using the Chrome ANGLE binaries.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WIN_D3DCOMPILER              "SDL_VIDEO_WIN_D3DCOMPILER"
```

## Remarks

SDL has EGL and OpenGL ES2 support on Windows via the ANGLE project. It can
use two different sets of binaries, those compiled by the user from source
or those provided by the Chrome browser. In the later case, these binaries
require that SDL loads a DLL providing the shader compiler.

The variable can be set to the following values:

- "d3dcompiler_46.dll" - best for Vista or later. (default)
- "d3dcompiler_43.dll" - for XP support.
- "none" - do not load any library, useful if you compiled ANGLE from
  source and included the compiler in your binaries.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

