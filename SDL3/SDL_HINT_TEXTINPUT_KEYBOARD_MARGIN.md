# SDL_HINT_TEXTINPUT_KEYBOARD_MARGIN

A variable controlling the spacing between the on-screen keyboard and text input areas.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_TEXTINPUT_KEYBOARD_MARGIN "SDL_TEXTINPUT_KEYBOARD_MARGIN"
```

## Remarks

This is the space, in window coordinates, to keep between the bottom of the
text input area and the top of the on-screen keyboard when the view is
moved to keep the text input area visible. This defaults to 0.

This hint sets the default value of
[SDL_PROP_TEXTINPUT_KEYBOARD_MARGIN_NUMBER](SDL_PROP_TEXTINPUT_KEYBOARD_MARGIN_NUMBER).

This hint should be set before calling
[SDL_StartTextInput](SDL_StartTextInput)() or
[SDL_StartTextInputWithProperties](SDL_StartTextInputWithProperties)().

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

