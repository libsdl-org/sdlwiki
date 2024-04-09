###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TextInputActive

Check whether or not Unicode text input events are enabled.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_TextInputActive(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if text input events are enabled else
[SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

