# SDL_HINT_RETURN_KEY_HIDES_IME

A variable to control whether the return key on the soft keyboard should hide the soft keyboard on Android and iOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RETURN_KEY_HIDES_IME "SDL_RETURN_KEY_HIDES_IME"
```

## Remarks

This hint sets the default value of
[SDL_PROP_TEXTINPUT_MULTILINE_BOOLEAN](SDL_PROP_TEXTINPUT_MULTILINE_BOOLEAN).

The variable can be set to the following values:

- "0": The return key will be handled as a key event. (default)
- "1": The return key will hide the keyboard.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

