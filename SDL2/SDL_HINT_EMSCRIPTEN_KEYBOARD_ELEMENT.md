###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT

override the binding element for keyboard inputs for Emscripten builds

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT   "SDL_EMSCRIPTEN_KEYBOARD_ELEMENT"
```

## Remarks

This hint only applies to the emscripten platform.

The variable can be one of:

- "#window": the javascript window object (this is the default)
- "#document": the javascript document object
- "#screen": the javascript window.screen object
- "#canvas": the WebGL canvas element

Any other string without a leading # sign applies to the element on the
page with that ID.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

