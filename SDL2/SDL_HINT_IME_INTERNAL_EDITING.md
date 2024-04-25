###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_IME_INTERNAL_EDITING

A variable to control whether certain IMEs should handle text editing internally instead of sending [SDL_TEXTEDITING](SDL_TEXTEDITING) events.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_INTERNAL_EDITING "SDL_IME_INTERNAL_EDITING"
```

## Remarks

The variable can be set to the following values:

- "0": [SDL_TEXTEDITING](SDL_TEXTEDITING) events are sent, and it is the
  application's responsibility to render the text from these events and
  differentiate it somehow from committed text. (default)
- "1": If supported by the IME then [SDL_TEXTEDITING](SDL_TEXTEDITING)
  events are not sent, and text that is being composed will be rendered in
  its own UI.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


