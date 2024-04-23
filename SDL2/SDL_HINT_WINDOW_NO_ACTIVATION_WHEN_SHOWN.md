###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOW_NO_ACTIVATION_WHEN_SHOWN

A variable controlling whether the window is activated when the [SDL_ShowWindow](SDL_ShowWindow) function is called

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOW_NO_ACTIVATION_WHEN_SHOWN    "SDL_WINDOW_NO_ACTIVATION_WHEN_SHOWN"
```

## Remarks

This variable can be set to the following values:

- "0": The window is activated when the [SDL_ShowWindow](SDL_ShowWindow)
  function is called
- "1": The window is not activated when the
  [SDL_ShowWindow](SDL_ShowWindow) function is called

By default SDL will activate the window when the
[SDL_ShowWindow](SDL_ShowWindow) function is called

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

