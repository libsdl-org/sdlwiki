# SDL_HINT_GDK_TEXTINPUT_TITLE

This variable sets the title of the TextInput window on GDK platforms.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GDK_TEXTINPUT_TITLE "SDL_GDK_TEXTINPUT_TITLE"
```

## Remarks

This hint is available only if [SDL_GDK_TEXTINPUT](SDL_GDK_TEXTINPUT)
defined.

This hint should be set before calling
[SDL_StartTextInput](SDL_StartTextInput)()

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

