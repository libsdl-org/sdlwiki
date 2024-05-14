###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_IME_SHOW_UI

A variable to control whether certain IMEs should show native UI components (such as the Candidate List) instead of suppressing them.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_SHOW_UI "SDL_IME_SHOW_UI"
```

## Remarks

The variable can be set to the following values:

- "0": Native UI components are not display. (default)
- "1": Native UI components are displayed.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

