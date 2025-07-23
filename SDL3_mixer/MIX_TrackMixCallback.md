###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_TrackMixCallback

A callback that fires when a [MIX_Track](MIX_Track) is mixing at various stages.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef void (SDLCALL *MIX_TrackMixCallback)(void *userdata, MIX_Track *track, const SDL_AudioSpec *spec, float *pcm, int samples);
```

## Function Parameters

|              |                                                             |
| ------------ | ----------------------------------------------------------- |
| **userdata** | an opaque pointer provided by the app for its personal use. |
| **track**    | the track that is being mixed.                              |
| **spec**     | the format of the data in `pcm`.                            |
| **pcm**      | the raw PCM data in float32 format.                         |
| **samples**  | the number of float values pointed to by `pcm`.             |

## Remarks

This callback is fired for different parts of the mixing pipeline, and
gives the app visbility into the audio data that is being generated at
various stages.

The audio data passed through here is _not_ const data; the app is
permitted to change it in any way it likes, and those changes will
propagate through the mixing pipeline.

An audiospec is provided. Different tracks might be in different formats,
and an app needs to be able to handle that, but SDL_mixer always does its
mixing work in 32-bit float samples, even if the inputs or final output are
not floating point. As such, `spec->format` will always be `SDL_AUDIO_F32`
and `pcm` hardcoded to be a float pointer.

`samples` is the number of float values pointed to by `pcm`: samples, not
sample frames! There are no promises how many samples will be provided
per-callback, and this number can vary wildly from call to call, depending
on many factors.

Making changes to the track during this callback is undefined behavior.
Change the data in `pcm` but not the track itself.

## Version

This datatype is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrackRawCallback](MIX_SetTrackRawCallback)
- [MIX_SetTrackCookedCallback](MIX_SetTrackCookedCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLMixer](CategorySDLMixer)

