###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO

A variable to control whether SDL will pause audio in background.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO "SDL_ANDROID_BLOCK_ON_PAUSE_PAUSEAUDIO"
```

## Remarks

The variable can be set to the following values:

- "0": Not paused, requires that
  [SDL_HINT_ANDROID_BLOCK_ON_PAUSE](SDL_HINT_ANDROID_BLOCK_ON_PAUSE) be set
  to "0"
- "1": Paused. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

