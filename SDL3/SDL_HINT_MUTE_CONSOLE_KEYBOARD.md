# SDL_HINT_MUTE_CONSOLE_KEYBOARD

A variable controlling whether the keyboard should be muted on the console.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MUTE_CONSOLE_KEYBOARD "SDL_MUTE_CONSOLE_KEYBOARD"
```

## Remarks

Normally the keyboard is muted while SDL applications are running so that
keyboard input doesn't show up as key strokes on the console. This hint
allows you to turn that off for debugging purposes.

The variable can be set to the following values:

- "0": Allow keystrokes to go through to the console.
- "1": Mute keyboard input so it doesn't show up on the console. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

