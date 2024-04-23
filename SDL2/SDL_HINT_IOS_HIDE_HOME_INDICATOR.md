###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_IOS_HIDE_HOME_INDICATOR

A variable controlling whether the home indicator bar on iPhone X should be hidden.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IOS_HIDE_HOME_INDICATOR "SDL_IOS_HIDE_HOME_INDICATOR"
```

## Remarks

This variable can be set to the following values:

- "0": The indicator bar is not hidden (default for windowed applications)
- "1": The indicator bar is hidden and is shown when the screen is touched
  (useful for movie playback applications)
- "2": The indicator bar is dim and the first swipe makes it visible and
  the second swipe performs the "home" action (default for fullscreen
  applications)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

