# SDL_HINT_VISIONOS_HDR_HEADROOM_UI

A variable controlling whether the HDR headroom slider should be shown in the visionOS window settings.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VISIONOS_HDR_HEADROOM_UI "SDL_VISIONOS_HDR_HEADROOM_UI"
```

## Remarks

The variable can be set to the following values:

- "0": The HDR headroom slider is not shown. (default)
- "1": The HDR headroom slider is shown.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

