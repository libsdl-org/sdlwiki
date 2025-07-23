###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PlayAudio

Play a [MIX_Audio](MIX_Audio) from start to finish without any management.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_PlayAudio(MIX_Mixer *mixer, MIX_Audio *audio);
```

## Function Parameters

|                          |           |                                        |
| ------------------------ | --------- | -------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer on which to play this audio. |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio input to play.               |

## Return Value

(bool) Returns true if the track has begun mixing, false on error; call
SDL_GetError() for details.

## Remarks

This is what we term a "fire-and-forget" sound. Internally, SDL_mixer will
manage a temporary track to mix the specified [MIX_Audio](MIX_Audio),
cleaning it up when complete. No options can be provided for how to do the
mixing, like [MIX_PlayTrack](MIX_PlayTrack)() offers, and since the track
is not available to the caller, no adjustments can be made to mixing over
time.

This is not the function to build an entire game of any complexity around,
but it can be convenient to play simple, one-off sounds that can't be
stopped early. An example would be a voice saying "GAME OVER" during an
unpausable endgame sequence.

There are no limits to the number of fire-and-forget sounds that can mix at
once (short of running out of memory), and SDL_mixer keeps an internal pool
of temporary tracks it creates as needed and reuses when available.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PlayTrack](MIX_PlayTrack)
- [MIX_LoadAudio](MIX_LoadAudio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

