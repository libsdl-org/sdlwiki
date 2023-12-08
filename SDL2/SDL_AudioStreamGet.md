###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioStreamGet

Get converted/resampled data from the stream

## Syntax

```c
int SDL_AudioStreamGet(SDL_AudioStream *stream, void *buf, int len);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **stream**     | The stream the audio is being requested from |
| **buf**        | A buffer to fill with audio data             |
| **len**        | The maximum number of bytes to fill          |

## Return Value

Returns the number of bytes read from the stream, or -1 on error

## Version

This function is available since SDL 2.0.7.

## Related Functions

* [SDL_NewAudioStream](SDL_NewAudioStream.md)
* [SDL_AudioStreamPut](SDL_AudioStreamPut.md)
* [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable.md)
* [SDL_AudioStreamFlush](SDL_AudioStreamFlush.md)
* [SDL_AudioStreamClear](SDL_AudioStreamClear.md)
* [SDL_FreeAudioStream](SDL_FreeAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
