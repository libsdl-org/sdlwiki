###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioStreamClear

Clear any pending data in the stream without converting it

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_AudioStreamClear(SDL_AudioStream *stream);
```

## Version

This function is available since SDL 2.0.7.

## See Also

- [SDL_NewAudioStream](SDL_NewAudioStream)
- [SDL_AudioStreamPut](SDL_AudioStreamPut)
- [SDL_AudioStreamGet](SDL_AudioStreamGet)
- [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable)
- [SDL_AudioStreamFlush](SDL_AudioStreamFlush)
- [SDL_FreeAudioStream](SDL_FreeAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

