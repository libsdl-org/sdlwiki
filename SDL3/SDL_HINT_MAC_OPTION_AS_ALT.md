# SDL_HINT_MAC_OPTION_AS_ALT

A variable controlling whether the Option (⌥) key on macOS should be remapped to act as the Alt key.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_OPTION_AS_ALT "SDL_MAC_OPTION_AS_ALT"
```

## Remarks

The variable can be set to the following values:

- "none": The Option key is not remapped to Alt. (default)
- "only_left": Only the left Option key is remapped to Alt.
- "only_right": Only the right Option key is remapped to Alt.
- "both": Both Option keys are remapped to Alt.

This will prevent the triggering of key compositions that rely on the
Option key, but will still send the Alt modifier for keyboard events. In
the case that both Alt and Option are pressed, the Option key will be
ignored. This is particularly useful for applications like terminal
emulators and graphical user interfaces (GUIs) that rely on Alt key
functionality for shortcuts or navigation. This does not apply to
[SDL_GetKeyFromScancode](SDL_GetKeyFromScancode) and only has an effect if
IME is enabled.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

