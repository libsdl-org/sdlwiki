# SDL_GetAudioStreamFrequencyRatio

Get the frequency ratio of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
float SDL_GetAudioStreamFrequencyRatio(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                                                  |
| ------------------------------------ | ---------- | ------------------------------------------------ |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the [SDL_AudioStream](SDL_AudioStream) to query. |

## Return Value

(float) Returns the frequency ratio of the stream or 0.0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetAudioStreamFrequencyRatio](SDL_SetAudioStreamFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

