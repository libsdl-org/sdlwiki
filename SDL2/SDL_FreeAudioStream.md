###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeAudioStream

Free an audio stream 

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_FreeAudioStream(SDL_AudioStream *stream);

```

## Version

This function is available since SDL 2.0.7.

## Related Functions

* [SDL_NewAudioStream](SDL_NewAudioStream)
* [SDL_AudioStreamPut](SDL_AudioStreamPut)
* [SDL_AudioStreamGet](SDL_AudioStreamGet)
* [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable)
* [SDL_AudioStreamFlush](SDL_AudioStreamFlush)
* [SDL_AudioStreamClear](SDL_AudioStreamClear)

----
[CategoryAPI](CategoryAPI)

