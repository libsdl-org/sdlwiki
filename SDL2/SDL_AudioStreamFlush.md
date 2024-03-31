###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioStreamFlush

Tell the stream that you're done sending data, and anything being buffered should be converted/resampled and made available immediately.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_AudioStreamFlush(SDL_AudioStream *stream);

```

## Remarks

It is legal to add more data to a stream after flushing, but there will be
audio gaps in the output. Generally this is intended to signal the end of
input, so the complete output becomes available.

## Version

This function is available since SDL 2.0.7.

## Related Functions

* [SDL_NewAudioStream](SDL_NewAudioStream)
* [SDL_AudioStreamPut](SDL_AudioStreamPut)
* [SDL_AudioStreamGet](SDL_AudioStreamGet)
* [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable)
* [SDL_AudioStreamClear](SDL_AudioStreamClear)
* [SDL_FreeAudioStream](SDL_FreeAudioStream)

----
[CategoryAPI](CategoryAPI)

