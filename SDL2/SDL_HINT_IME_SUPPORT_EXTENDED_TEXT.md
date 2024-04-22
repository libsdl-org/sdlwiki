###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_IME_SUPPORT_EXTENDED_TEXT

A variable to control if extended IME text support is enabled.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_IME_SUPPORT_EXTENDED_TEXT "SDL_IME_SUPPORT_EXTENDED_TEXT"
```

## Remarks

If enabled then [SDL_TextEditingExtEvent](SDL_TextEditingExtEvent) will be
issued if the text would be truncated otherwise. Additionally
[SDL_TextInputEvent](SDL_TextInputEvent) will be dispatched multiple times
so that it is not truncated.

The variable can be set to the following values: "0" - Legacy behavior.
Text can be truncated, no heap allocations. (default) "1" - Modern
behavior.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

