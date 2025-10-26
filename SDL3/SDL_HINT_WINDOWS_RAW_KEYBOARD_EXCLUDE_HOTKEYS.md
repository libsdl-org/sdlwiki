# SDL_HINT_WINDOWS_RAW_KEYBOARD_EXCLUDE_HOTKEYS

A variable controlling whether or not the RIDEV_NOHOTKEYS flag is set when enabling Windows raw keyboard events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_RAW_KEYBOARD_EXCLUDE_HOTKEYS "SDL_WINDOWS_RAW_KEYBOARD_EXCLUDE_HOTKEYS"
```

## Remarks

This blocks any hotkeys that have been registered by applications from
having any effect beyond generating raw WM_INPUT events.

This flag does not affect system-hotkeys like ALT-TAB or CTRL-ALT-DEL, but
does affect the Windows Logo key since it is a userland hotkey registered
by explorer.exe.

The variable can be set to the following values:

- "0": Hotkeys are not excluded. (default)
- "1": Hotkeys are excluded.

This hint can be set anytime.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

