###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RETURN_KEY_HIDES_IME

A variable to control whether the return key on the soft keyboard should hide the soft keyboard on Android and iOS.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RETURN_KEY_HIDES_IME "SDL_RETURN_KEY_HIDES_IME"
```

## Remarks

The variable can be set to the following values:

- "0": The return key will be handled as a key event. This is the behaviour
  of SDL <= 2.0.3. (default)
- "1": The return key will hide the keyboard.

The value of this hint is used at runtime, so it can be changed at any
time.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

