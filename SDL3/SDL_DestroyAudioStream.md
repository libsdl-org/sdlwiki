# SDL_DestroyAudioStream

Free an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
void SDL_DestroyAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                              |
| ------------------------------------ | ---------- | ---------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to destroy. |

## Remarks

This will release all allocated data, including any audio that is still
queued. You do not need to manually clear the stream first.

If this stream was bound to an audio device, it is unbound during this
call. If this stream was created with
[SDL_OpenAudioDeviceStream](SDL_OpenAudioDeviceStream), the audio device
that was opened alongside this stream's creation will be closed, too.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateAudioStream](SDL_CreateAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

