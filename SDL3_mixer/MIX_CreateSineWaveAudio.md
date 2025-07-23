###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_CreateSineWaveAudio

Create a [MIX_Audio](MIX_Audio) that generates a sinewave.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_CreateSineWaveAudio(MIX_Mixer *mixer, int hz, float amplitude);
```

## Function Parameters

|                          |               |                                                              |
| ------------------------ | ------------- | ------------------------------------------------------------ |
| [MIX_Mixer](MIX_Mixer) * | **mixer**     | a mixer this audio is intended to be used with. May be NULL. |
| int                      | **hz**        | the sinewave's frequency in Hz.                              |
| float                    | **amplitude** | the sinewave's amplitude from 0.0f to 1.0f.                  |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns an audio object that can be used to make
sound on a mixer, or NULL on failure; call SDL_GetError() for more
information.

## Remarks

This is useful just to have _something_ to play, perhaps for testing or
debugging purposes.

The resulting [MIX_Audio](MIX_Audio) will generate infinite audio when
assigned to a track.

You specify its frequency in Hz (determines the pitch of the sinewave's
audio) and amplitude (determines the volume of the sinewave: 1.0f is very
loud, 0.0f is silent).

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
- [MIX_LoadAudio_IO](MIX_LoadAudio_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

