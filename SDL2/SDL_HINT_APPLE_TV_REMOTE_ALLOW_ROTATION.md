###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_APPLE_TV_REMOTE_ALLOW_ROTATION

A variable controlling whether the Apple TV remote's joystick axes will automatically match the rotation of the remote.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APPLE_TV_REMOTE_ALLOW_ROTATION "SDL_APPLE_TV_REMOTE_ALLOW_ROTATION"
```

## Remarks

This variable can be set to the following values:

- "0": Remote orientation does not affect joystick axes (the default).
- "1": Joystick axes are based on the orientation of the remote.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

