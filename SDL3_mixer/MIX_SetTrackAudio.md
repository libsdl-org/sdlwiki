###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackAudio

Set a [MIX_Track](MIX_Track)'s input to a [MIX_Audio](MIX_Audio).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackAudio(MIX_Track *track, MIX_Audio *audio);
```

## Function Parameters

|                          |           |                                              |
| ------------------------ | --------- | -------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track on which to set a new audio input. |
| [MIX_Audio](MIX_Audio) * | **audio** | the new audio input to set. May be NULL.     |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

A [MIX_Audio](MIX_Audio) is audio data stored in RAM (possibly still in a
compressed form). One [MIX_Audio](MIX_Audio) can be assigned to multiple
tracks at once.

Once a track has a valid input, it can start mixing sound by calling
[MIX_PlayTrack](MIX_PlayTrack)(), or possibly [MIX_PlayTag](MIX_PlayTag)().

Calling this function with a NULL audio input is legal, and removes any
input from the track. If the track was currently playing, the next time the
mixer runs, it'll notice this and mark the track as stopped, calling any
assigned [MIX_TrackStoppedCallback](MIX_TrackStoppedCallback).

It is legal to change the input of a track while it's playing, however some
states, like loop points, may cease to make sense with the new audio. In
such a case, one can call [MIX_PlayTrack](MIX_PlayTrack) again to adjust
parameters.

The track will hold a reference to the provided [MIX_Audio](MIX_Audio), so
it is safe to call [MIX_DestroyAudio](MIX_DestroyAudio)() on it while the
track is still using it. The track will drop its reference (and possibly
free the resources) once it is no longer using the [MIX_Audio](MIX_Audio).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

