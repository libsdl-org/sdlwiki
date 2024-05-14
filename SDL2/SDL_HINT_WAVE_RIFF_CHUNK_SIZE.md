###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WAVE_RIFF_CHUNK_SIZE

Controls how the size of the RIFF chunk affects the loading of a WAVE file.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WAVE_RIFF_CHUNK_SIZE   "SDL_WAVE_RIFF_CHUNK_SIZE"
```

## Remarks

The size of the RIFF chunk (which includes all the sub-chunks of the WAVE
file) is not always reliable. In case the size is wrong, it's possible to
just ignore it and step through the chunks until a fixed limit is reached.

Note that files that have trailing data unrelated to the WAVE file or
corrupt files may slow down the loading process without a reliable
boundary. By default, SDL stops after 10000 chunks to prevent wasting time.
Use the environment variable [SDL_WAVE_CHUNK_LIMIT](SDL_WAVE_CHUNK_LIMIT)
to adjust this value.

This variable can be set to the following values:

- "force": Always use the RIFF chunk size as a boundary for the chunk
  search
- "ignorezero": Like "force", but a zero size searches up to 4 GiB
  (default)
- "ignore": Ignore the RIFF chunk size and always search up to 4 GiB
- "maximum": Search for chunks until the end of file (not recommended)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

