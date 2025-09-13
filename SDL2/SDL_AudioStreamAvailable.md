# SDL_AudioStreamAvailable

Get the number of converted/resampled bytes available.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
int SDL_AudioStreamAvailable(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                            |
| ------------------------------------ | ---------- | -------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to query. |

## Return Value

(int) Returns the number of bytes available.

## Remarks

The stream may be buffering data behind the scenes until it has enough to
resample correctly, so this number might be lower than what you expect, or
even be zero. Add more data or flush the stream if you need the data now.

## Version

This function is available since SDL 2.0.7.

## See Also

- [SDL_NewAudioStream](SDL_NewAudioStream)
- [SDL_AudioStreamPut](SDL_AudioStreamPut)
- [SDL_AudioStreamGet](SDL_AudioStreamGet)
- [SDL_AudioStreamFlush](SDL_AudioStreamFlush)
- [SDL_AudioStreamClear](SDL_AudioStreamClear)
- [SDL_FreeAudioStream](SDL_FreeAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

