###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_TV_REMOTE_AS_JOYSTICK

A variable controlling whether the Android / tvOS remotes should be listed as joystick devices, instead of sending keyboard events.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_TV_REMOTE_AS_JOYSTICK "SDL_TV_REMOTE_AS_JOYSTICK"
```

## Remarks

This variable can be set to the following values:

- "0": Remotes send enter/escape/arrow key events
- "1": Remotes are available as 2 axis, 2 button joysticks (the default).

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

