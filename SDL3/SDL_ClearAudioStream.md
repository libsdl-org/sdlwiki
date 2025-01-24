# SDL_ClearAudioStream

Clear any pending data in the stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_ClearAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                            |
| ------------------------------------ | ---------- | -------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to clear. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This drops any queued data, so there will be nothing to read from the
stream until more is added.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
- [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
- [SDL_GetAudioStreamQueued](SDL_GetAudioStreamQueued)
- [SDL_PutAudioStreamData](SDL_PutAudioStreamData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

