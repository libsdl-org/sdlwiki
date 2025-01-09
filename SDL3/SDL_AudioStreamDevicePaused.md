###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AudioStreamDevicePaused

Use this function to query if an audio device associated with a stream is paused.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_AudioStreamDevicePaused(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                                                             |
| ------------------------------------ | ---------- | ----------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream associated with the audio device to query. |

## Return Value

(bool) Returns true if device is valid and paused, false otherwise.

## Remarks

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PauseAudioStreamDevice](SDL_PauseAudioStreamDevice)
- [SDL_ResumeAudioStreamDevice](SDL_ResumeAudioStreamDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

