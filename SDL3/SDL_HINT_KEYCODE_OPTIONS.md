###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_KEYCODE_OPTIONS

A variable that controls keycode representation in keyboard events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_KEYCODE_OPTIONS "SDL_KEYCODE_OPTIONS"
```

## Remarks

This variable is a comma separated set of options for translating keycodes
in events:

- "none": Keycode options are cleared, this overrides other options.
- "hide_numpad": The numpad keysyms will be translated into their
  non-numpad versions based on the current NumLock state. For example,
  [SDLK_KP_4](SDLK_KP_4) would become [SDLK_4](SDLK_4) if
  [SDL_KMOD_NUM](SDL_KMOD_NUM) is set in the event modifiers, and
  [SDLK_LEFT](SDLK_LEFT) if it is unset.
- "french_numbers": The number row on French keyboards is inverted, so
  pressing the 1 key would yield the keycode [SDLK_1](SDLK_1), or '1',
  instead of [SDLK_AMPERSAND](SDLK_AMPERSAND), or '&'
- "latin_letters": For keyboards using non-Latin letters, such as Russian
  or Thai, the letter keys generate keycodes as though it had an en_US
  layout. e.g. pressing the key associated with
  [SDL_SCANCODE_A](SDL_SCANCODE_A) on a Russian keyboard would yield 'a'
  instead of 'ф'.

The default value for this hint is "french_numbers"

Some platforms like Emscripten only provide modified keycodes and the
options are not used.

These options do not affect the return value of
[SDL_GetKeyFromScancode](SDL_GetKeyFromScancode)() or
[SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)(), they just apply to the
keycode included in key events.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

