###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_GDK_TEXTINPUT_MAX_LENGTH

This variable sets the maximum input length of the TextInput window on GDK platforms.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_GDK_TEXTINPUT_MAX_LENGTH "SDL_GDK_TEXTINPUT_MAX_LENGTH"
```

## Remarks

The value must be a stringified integer, for example "10" to allow for up
to 10 characters of text input.

This hint is available only if [SDL_GDK_TEXTINPUT](SDL_GDK_TEXTINPUT)
defined.

This hint should be set before calling
[SDL_StartTextInput](SDL_StartTextInput)()

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

