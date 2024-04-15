###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_IME_INTERNAL_EDITING

A variable to control whether certain IMEs should handle text editing internally instead of sending [SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) events.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_IME_INTERNAL_EDITING "SDL_IME_INTERNAL_EDITING"
```

## Remarks

The variable can be set to the following values:

- "0": [SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) events are sent,
  and it is the application's responsibility to render the text from these
  events and differentiate it somehow from committed text. (default)
- "1": If supported by the IME then
  [SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) events are not sent, and
  text that is being composed will be rendered in its own UI.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


