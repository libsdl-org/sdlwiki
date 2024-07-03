###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamGain

Change the gain of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_SetAudioStreamGain(SDL_AudioStream *stream, float gain);
```

## Function Parameters

|                                      |            |                                                |
| ------------------------------------ | ---------- | ---------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the stream on which the gain is being changed. |
| float                                | **gain**   | the gain. 1.0f is no change, 0.0f is silence.  |

## Return Value

(int) Returns 0 on success, or -1 on error.

## Remarks

The gain of a stream is its volume; a larger gain means a louder output,
with a gain of zero being silence.

Audio streams default to a gain of 1.0f (no change in output).

This is applied during [SDL_GetAudioStreamData](SDL_GetAudioStreamData),
and can be continuously changed to create various effects.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAudioStreamGain](SDL_GetAudioStreamGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

