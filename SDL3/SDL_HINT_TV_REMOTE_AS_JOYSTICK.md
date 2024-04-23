###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_TV_REMOTE_AS_JOYSTICK

A variable controlling whether the Android / tvOS remotes should be listed as joystick devices, instead of sending keyboard events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_TV_REMOTE_AS_JOYSTICK "SDL_TV_REMOTE_AS_JOYSTICK"
```

## Remarks

The variable can be set to the following values:

- "0": Remotes send enter/escape/arrow key events.
- "1": Remotes are available as 2 axis, 2 button joysticks. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

