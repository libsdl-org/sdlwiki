###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WAVE_TRUNCATION

A variable controlling how a truncated WAVE file is handled.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_WAVE_TRUNCATION   "SDL_WAVE_TRUNCATION"
```

## Remarks

A WAVE file is considered truncated if any of the chunks are incomplete or
the data chunk size is not a multiple of the block size. By default, SDL
decodes until the first incomplete block, as most applications seem to do.

The variable can be set to the following values:

- "verystrict" - Raise an error if the file is truncated.
- "strict" - Like "verystrict", but the size of the RIFF chunk is ignored.
- "dropframe" - Decode until the first incomplete sample frame.
- "dropblock" - Decode until the first incomplete block. (default)

This hint should be set before calling [SDL_LoadWAV](SDL_LoadWAV)() or
[SDL_LoadWAV_IO](SDL_LoadWAV_IO)()

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

