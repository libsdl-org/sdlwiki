###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_LoadRawAudio_IO

Load raw PCM data from an SDL_IOStream.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_LoadRawAudio_IO(MIX_Mixer *mixer, SDL_IOStream *io, const SDL_AudioSpec *spec, bool closeio);
```

## Function Parameters

|                          |             |                                                                            |
| ------------------------ | ----------- | -------------------------------------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer**   | a mixer this audio is intended to be used with. May be NULL.               |
| SDL_IOStream *           | **io**      | the SDL_IOStream to load data from.                                        |
| const SDL_AudioSpec *    | **spec**    | what format the raw data is in.                                            |
| bool                     | **closeio** | true if SDL_mixer should close `io` before returning (success or failure). |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns an audio object that can be used to make
sound on a mixer, or NULL on failure; call SDL_GetError() for more
information.

## Remarks

There are other options for _streaming_ raw PCM: an SDL_AudioStream can be
connected to a track, as can an SDL_IOStream, and will read from those
sources on-demand when it is time to mix the audio. This function is useful
for loading static audio data that is meant to be played multiple times.

This function will load the raw data in its entirety and cache it in RAM.

[MIX_Audio](MIX_Audio) objects can be shared between multiple mixers. The
`mixer` parameter just suggests the most likely mixer to use this audio, in
case some optimization might be applied, but this is not required, and a
NULL mixer may be specified.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_DestroyAudio](MIX_DestroyAudio)
- [MIX_SetTrackAudio](MIX_SetTrackAudio)
- [MIX_LoadRawAudio](MIX_LoadRawAudio)
- [MIX_LoadRawAudioNoCopy](MIX_LoadRawAudioNoCopy)
- [MIX_LoadAudio_IO](MIX_LoadAudio_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

