###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO

A variable to control whether SDL will pause audio in background (Requires [SDL_ANDROID_BLOCK_ON_PAUSE](SDL_ANDROID_BLOCK_ON_PAUSE) as "Non blocking")

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO "SDL_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO"
```

## Remarks

The variable can be set to the following values: "0" - Non paused. "1" -
Paused. (default)

The value should be set before SDL is initialized.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

