###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioStreamFlush

Tell the stream that you're done sending data, and anything being buffered should be converted/resampled and made available immediately.

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

* [SDL_NewAudioStream](SDL_NewAudioStream.md)
* [SDL_AudioStreamPut](SDL_AudioStreamPut.md)
* [SDL_AudioStreamGet](SDL_AudioStreamGet.md)
* [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable.md)
* [SDL_AudioStreamClear](SDL_AudioStreamClear.md)
* [SDL_FreeAudioStream](SDL_FreeAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
