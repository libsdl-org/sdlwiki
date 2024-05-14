###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_IME_SHOW_UI

A variable to control whether certain IMEs should show native UI components (such as the Candidate List) instead of suppressing them.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_SHOW_UI "SDL_IME_SHOW_UI"
```

## Remarks

The variable can be set to the following values:

- "0": Native UI components are not display. (default)
- "1": Native UI components are displayed.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

