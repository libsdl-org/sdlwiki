###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WAVE_TRUNCATION

Controls how a truncated WAVE file is handled.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WAVE_TRUNCATION   "SDL_WAVE_TRUNCATION"
```

## Remarks

A WAVE file is considered truncated if any of the chunks are incomplete or
the data chunk size is not a multiple of the block size. By default, SDL
decodes until the first incomplete block, as most applications seem to do.

This variable can be set to the following values:

- "verystrict": Raise an error if the file is truncated
- "strict": Like "verystrict", but the size of the RIFF chunk is ignored
- "dropframe": Decode until the first incomplete sample frame
- "dropblock": Decode until the first incomplete block (default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

