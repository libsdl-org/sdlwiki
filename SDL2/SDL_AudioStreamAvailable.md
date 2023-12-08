###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioStreamAvailable

Get the number of converted/resampled bytes available.

## Syntax

```c
int SDL_AudioStreamAvailable(SDL_AudioStream *stream);

```

## Remarks

The stream may be buffering data behind the scenes until it has enough to
resample correctly, so this number might be lower than what you expect, or
even be zero. Add more data or flush the stream if you need the data now.

## Version

This function is available since SDL 2.0.7.

## Related Functions

* [SDL_NewAudioStream](SDL_NewAudioStream.md)
* [SDL_AudioStreamPut](SDL_AudioStreamPut.md)
* [SDL_AudioStreamGet](SDL_AudioStreamGet.md)
* [SDL_AudioStreamFlush](SDL_AudioStreamFlush.md)
* [SDL_AudioStreamClear](SDL_AudioStreamClear.md)
* [SDL_FreeAudioStream](SDL_FreeAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
