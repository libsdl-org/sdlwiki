###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_IDLE_TIMER_DISABLED

A variable controlling whether the idle timer is disabled on iOS.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IDLE_TIMER_DISABLED "SDL_IOS_IDLE_TIMER_DISABLED"
```

## Remarks

When an iOS app does not receive touches for some time, the screen is
dimmed automatically. For games where the accelerometer is the only input
this is problematic. This functionality can be disabled by setting this
hint.

As of SDL 2.0.4, [SDL_EnableScreenSaver](SDL_EnableScreenSaver)() and
[SDL_DisableScreenSaver](SDL_DisableScreenSaver)() accomplish the same
thing on iOS. They should be preferred over this hint.

This variable can be set to the following values:

- "0": Enable idle timer
- "1": Disable idle timer

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

