###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GroupMixCallback

A callback that fires when a [MIX_Group](MIX_Group) has completed mixing.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef void (SDLCALL *MIX_GroupMixCallback)(void *userdata, MIX_Group *group, const SDL_AudioSpec *spec, float *pcm, int samples);
```

## Function Parameters

|              |                                                             |
| ------------ | ----------------------------------------------------------- |
| **userdata** | an opaque pointer provided by the app for its personal use. |
| **group**    | the group that is being mixed.                              |
| **spec**     | the format of the data in `pcm`.                            |
| **pcm**      | the raw PCM data in float32 format.                         |
| **samples**  | the number of float values pointed to by `pcm`.             |

## Remarks

This callback is fired when a mixing group has finished mixing: all tracks
in the group have mixed into a single buffer and are prepared to be mixed
into all other groups for the final mix output.

The audio data passed through here is _not_ const data; the app is
permitted to change it in any way it likes, and those changes will
propagate through the mixing pipeline.

An audiospec is provided. Different groups might be in different formats,
and an app needs to be able to handle that, but SDL_mixer always does its
mixing work in 32-bit float samples, even if the inputs or final output are
not floating point. As such, `spec->format` will always be `SDL_AUDIO_F32`
and `pcm` hardcoded to be a float pointer.

`samples` is the number of float values pointed to by `pcm`: samples, not
sample frames! There are no promises how many samples will be provided
per-callback, and this number can vary wildly from call to call, depending
on many factors.

## Version

This datatype is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetGroupPostMixCallback](MIX_SetGroupPostMixCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLMixer](CategorySDLMixer)

