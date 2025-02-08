# SDL_HINT_GRAB_KEYBOARD

A variable controlling whether grabbing input grabs the keyboard

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GRAB_KEYBOARD              "SDL_GRAB_KEYBOARD"
```

## Remarks

This variable can be set to the following values:

- "0": Grab will affect only the mouse
- "1": Grab will affect mouse and keyboard

By default SDL will not grab the keyboard so system shortcuts still work.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

