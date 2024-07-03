###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioPostmixCallback

A callback that fires when data is about to be fed to an audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
typedef void (SDLCALL *SDL_AudioPostmixCallback)(void *userdata, const SDL_AudioSpec *spec, float *buffer, int buflen);
```

## Function Parameters

|              |                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| **userdata** | a pointer provided by the app through [SDL_SetAudioPostmixCallback](SDL_SetAudioPostmixCallback), for its own use. |
| **spec**     | the current format of audio that is to be submitted to the audio device.                                           |
| **buffer**   | the buffer of audio samples to be submitted. The callback can inspect and/or modify this data.                     |
| **buflen**   | the size of `buffer` in bytes.                                                                                     |

## Remarks

This is useful for accessing the final mix, perhaps for writing a
visualizer or applying a final effect to the audio data before playback.

This callback should run as quickly as possible and not block for any
significant time, as this callback delays submission of data to the audio
device, which can cause audio playback problems.

The postmix callback _must_ be able to handle any audio data format
specified in `spec`, which can change between callbacks if the audio device
changed. However, this only covers frequency and channel count; data is
always provided here in [SDL_AUDIO_F32](SDL_AUDIO_F32) format.

The postmix callback runs _after_ logical device gain and audiostream gain
have been applied, which is to say you can make the output data louder at
this point than the gain settings would suggest.

## Thread Safety

This will run from a background thread owned by SDL. The application is
responsible for locking resources the callback touches that need to be
protected.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_SetAudioPostmixCallback](SDL_SetAudioPostmixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAudio](CategoryAudio)

