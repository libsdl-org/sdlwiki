###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_IME_IMPLEMENTED_UI

A variable describing what IME UI elements the application can display.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_IMPLEMENTED_UI "SDL_IME_IMPLEMENTED_UI"
```

## Remarks

By default IME UI is handled using native components by the OS where
possible, however this can interfere with or not be visible when exclusive
fullscreen mode is used.

The variable can be set to a comma separated list containing the following
items:

- "none" or "0": The application can't render any IME elements, and native
  UI should be used. (default)
- "composition": The application handles
  [SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) events and can render
  the composition text.
- "candidates": The application handles
  [SDL_EVENT_TEXT_EDITING_CANDIDATES](SDL_EVENT_TEXT_EDITING_CANDIDATES)
  and can render the candidate list.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

