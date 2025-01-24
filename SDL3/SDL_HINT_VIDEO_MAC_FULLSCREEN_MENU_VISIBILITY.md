# SDL_HINT_VIDEO_MAC_FULLSCREEN_MENU_VISIBILITY

A variable that specifies the menu visibility when a window is fullscreen in Spaces on macOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_MAC_FULLSCREEN_MENU_VISIBILITY "SDL_VIDEO_MAC_FULLSCREEN_MENU_VISIBILITY"
```

## Remarks

The variable can be set to the following values:

- "0": The menu will be hidden when the window is in a fullscreen space,
  and not accessible by moving the mouse to the top of the screen.
- "1": The menu will be accessible when the window is in a fullscreen
  space.
- "auto": The menu will be hidden if fullscreen mode was toggled on
  programmatically via `SDL_SetWindowFullscreen()`, and accessible if
  fullscreen was entered via the "fullscreen" button on the window title
  bar. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

