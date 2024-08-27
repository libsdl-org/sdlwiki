###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearAudioStream

Clear any pending data in the stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_bool SDL_ClearAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                            |
| ------------------------------------ | ---------- | -------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to clear. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This drops any queued data, so there will be nothing to read from the
stream until more is added.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
- [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
- [SDL_GetAudioStreamQueued](SDL_GetAudioStreamQueued)
- [SDL_PutAudioStreamData](SDL_PutAudioStreamData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

