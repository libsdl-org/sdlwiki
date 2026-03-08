# SDL_HINT_WINDOWS_RAW_KEYBOARD_INPUTSINK

A variable controlling whether the RIDEV_INPUTSINK flag is set when enabling Windows raw keyboard events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_RAW_KEYBOARD_INPUTSINK "SDL_WINDOWS_RAW_KEYBOARD_INPUTSINK"
```

## Remarks

This enables the window to still receive input even if not in foreground.

Focused windows that receive text input will still prevent input events
from triggering.

- "0": Input is not received when not in focus or foreground. (default)
- "1": Input will be received even when not in focus or foreground.

This hint can be set anytime.

## Version

This hint is available since SDL 3.4.4.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

