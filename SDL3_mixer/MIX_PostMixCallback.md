###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PostMixCallback

A callback that fires when all mixing has completed.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef void (SDLCALL *MIX_PostMixCallback)(void *userdata, MIX_Mixer *mixer, const SDL_AudioSpec *spec, float *pcm, int samples);
```

## Function Parameters

|              |                                                             |
| ------------ | ----------------------------------------------------------- |
| **userdata** | an opaque pointer provided by the app for its personal use. |
| **mixer**    | the mixer that is generating audio.                         |
| **spec**     | the format of the data in `pcm`.                            |
| **pcm**      | the raw PCM data in float32 format.                         |
| **samples**  | the number of float values pointed to by `pcm`.             |

## Remarks

This callback is fired when the mixer has completed all its work. If this
mixer was created with [MIX_CreateMixerDevice](MIX_CreateMixerDevice)(),
the data provided by this callback is what is being sent to the audio
hardware, minus last conversions for format requirements. If this mixer was
created with [MIX_CreateMixer](MIX_CreateMixer)(), this is what is being
output from [MIX_Generate](MIX_Generate)(), after final conversions.

The audio data passed through here is _not_ const data; the app is
permitted to change it in any way it likes, and those changes will replace
the final mixer pipeline output.

An audiospec is provided. SDL_mixer always does its mixing work in 32-bit
float samples, even if the inputs or final output are not floating point.
As such, `spec->format` will always be `SDL_AUDIO_F32` and `pcm` hardcoded
to be a float pointer.

`samples` is the number of float values pointed to by `pcm`: samples, not
sample frames! There are no promises how many samples will be provided
per-callback, and this number can vary wildly from call to call, depending
on many factors.

## Version

This datatype is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetPostMixCallback](MIX_SetPostMixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLMixer](CategorySDLMixer)

