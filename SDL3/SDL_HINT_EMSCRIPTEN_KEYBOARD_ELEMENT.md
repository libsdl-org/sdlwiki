###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT

Override the binding element for keyboard inputs for Emscripten builds.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT   "SDL_EMSCRIPTEN_KEYBOARD_ELEMENT"
```

## Remarks

This hint only applies to the emscripten platform.

The variable can be one of:

- "#window": the javascript window object (default)
- "#document": the javascript document object
- "#screen": the javascript window.screen object
- "#canvas": the WebGL canvas element
- any other string without a leading # sign applies to the element on the
  page with that ID.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

