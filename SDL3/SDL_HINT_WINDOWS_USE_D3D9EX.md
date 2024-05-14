###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_USE_D3D9EX

A variable controlling whether SDL uses the D3D9Ex API introduced in Windows Vista, instead of normal D3D9.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_USE_D3D9EX "SDL_WINDOWS_USE_D3D9EX"
```

## Remarks

Direct3D 9Ex contains changes to state management that can eliminate device
loss errors during scenarios like Alt+Tab or UAC prompts. D3D9Ex may
require some changes to your application to cope with the new behavior, so
this is disabled by default.

For more information on Direct3D 9Ex, see:

- https://docs.microsoft.com/en-us/windows/win32/direct3darticles/graphics-apis-in-windows-vista#direct3d-9ex
- https://docs.microsoft.com/en-us/windows/win32/direct3darticles/direct3d-9ex-improvements

The variable can be set to the following values:

- "0": Use the original Direct3D 9 API. (default)
- "1": Use the Direct3D 9Ex API on Vista and later (and fall back if D3D9Ex
  is unavailable)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

