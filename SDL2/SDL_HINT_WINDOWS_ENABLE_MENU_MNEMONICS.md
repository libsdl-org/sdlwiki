###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_ENABLE_MENU_MNEMONICS

Controls whether menus can be opened with their keyboard shortcut (Alt+mnemonic).

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_ENABLE_MENU_MNEMONICS "SDL_WINDOWS_ENABLE_MENU_MNEMONICS"
```

## Remarks

If the mnemonics are enabled, then menus can be opened by pressing the Alt
key and the corresponding mnemonic (for example, Alt+F opens the File
menu). However, in case an invalid mnemonic is pressed, Windows makes an
audible beep to convey that nothing happened. This is true even if the
window has no menu at all!

Because most SDL applications don't have menus, and some want to use the
Alt key for other purposes, SDL disables mnemonics (and the beeping) by
default.

Note: This also affects keyboard events: with mnemonics enabled, when a
menu is opened from the keyboard, you will not receive a KEYUP event for
the mnemonic key, and *might* not receive one for Alt.

This variable can be set to the following values:

- "0": Alt+mnemonic does nothing, no beeping. (default)
- "1": Alt+mnemonic opens menus, invalid mnemonics produce a beep.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

