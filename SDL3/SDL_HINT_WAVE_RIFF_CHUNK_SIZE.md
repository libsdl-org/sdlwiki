###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WAVE_RIFF_CHUNK_SIZE

A variable controlling how the size of the RIFF chunk affects the loading of a WAVE file.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

The variable can be set to the following values:

- "force" - Always use the RIFF chunk size as a boundary for the chunk
  search.
- "ignorezero" - Like "force", but a zero size searches up to 4 GiB.
  (default)
- "ignore" - Ignore the RIFF chunk size and always search up to 4 GiB.
- "maximum" - Search for chunks until the end of file. (not recommended)

This hint should be set before calling [SDL_LoadWAV](SDL_LoadWAV)() or
[SDL_LoadWAV_IO](SDL_LoadWAV_IO)()

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

