###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PauseAudioStreamDevice

Use this function to pause audio playback on the audio device associated with an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_PauseAudioStreamDevice(SDL_AudioStream *stream);
```

## Function Parameters

|                |                                                            |
| -------------- | ---------------------------------------------------------- |
| **stream**     | The audio stream associated with the audio device to pause |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function pauses audio processing for a given device. Any bound audio
streams will not progress, and no audio will be generated. Pausing one
device does not prevent other unpaused devices from running.

Pausing a device can be useful to halt all audio without unbinding all the
audio streams. This might be useful while a game is paused, or a level is
loading, etc.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ResumeAudioStreamDevice](SDL_ResumeAudioStreamDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

