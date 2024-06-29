###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_IME_NATIVE_UI

A variable describing what IME elements the OS should render natively over the game.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_NATIVE_UI "SDL_IME_NATIVE_UI"
```

## Remarks

By default IME UI is handled using native components by the OS, however
this interferes with fullscreen games in some cases.

The variable can be set to a comma separated list containing the following
items:

- "none" or "0": Native UI elements will not be displayed.
- "composition": Native UI elements will be used for the IME composition
  string.
- "candidates": Native UI elements will be used for the IME candidate list.
- "all" or "1": Native UI elements will be used for all IME UI. (default)

If native UI is used for the composition string, then
[SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) will not be sent.

If native UI is used for the candidates list, then
[SDL_EVENT_TEXT_EDITING_CANDIDATES](SDL_EVENT_TEXT_EDITING_CANDIDATES) will
not be sent.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

