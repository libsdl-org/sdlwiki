###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ResumeAudioStreamDevice

Use this function to unpause audio playback on the audio device associated with an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_ResumeAudioStreamDevice(SDL_AudioStream *stream);
```

## Function Parameters

|                |                                                             |
| -------------- | ----------------------------------------------------------- |
| **stream**     | The audio stream associated with the audio device to resume |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unpauses audio processing for a given device that has
previously been paused. Once unpaused, any bound audio streams will begin
to progress again, and audio can be generated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PauseAudioStreamDevice](SDL_PauseAudioStreamDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

