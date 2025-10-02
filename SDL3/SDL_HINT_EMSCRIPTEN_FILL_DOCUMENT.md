# SDL_HINT_EMSCRIPTEN_FILL_DOCUMENT

Dictate that newly-created windows will fill the whole browser window.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EMSCRIPTEN_FILL_DOCUMENT "SDL_EMSCRIPTEN_FILL_DOCUMENT"
```

## Remarks

The canvas element fills the entire document. Resize events will be
generated as the browser window is resized, as that will adjust the canvas
size as well. The canvas will cover anything else on the page, including
any controls provided by Emscripten in its generated HTML file. Often times
this is desirable for a browser-based game, but it means several things
that we expect of an SDL window on other platforms might not work as
expected, such as minimum window sizes and aspect ratios.

This hint overrides
[SDL_PROP_WINDOW_CREATE_EMSCRIPTEN_FILL_DOCUMENT_BOOLEAN](SDL_PROP_WINDOW_CREATE_EMSCRIPTEN_FILL_DOCUMENT_BOOLEAN)
properties when creating an SDL window.

This hint only applies to the emscripten platform.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

