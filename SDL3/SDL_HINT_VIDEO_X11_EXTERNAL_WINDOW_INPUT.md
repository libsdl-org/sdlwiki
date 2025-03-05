# SDL_HINT_VIDEO_X11_EXTERNAL_WINDOW_INPUT

A variable controlling whether SDL should call XSelectInput() to enable input events on X11 windows wrapped by SDL windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_EXTERNAL_WINDOW_INPUT "SDL_VIDEO_X11_EXTERNAL_WINDOW_INPUT"
```

## Remarks

The variable can be set to the following values:

- "0": Don't call XSelectInput(), assuming the native window code has done
  it already.
- "1": Call XSelectInput() to enable input events. (default)

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.2.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

