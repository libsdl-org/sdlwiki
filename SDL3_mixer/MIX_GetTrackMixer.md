###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackMixer

Get the [MIX_Mixer](MIX_Mixer) that owns a [MIX_Track](MIX_Track).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Mixer * MIX_GetTrackMixer(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

([MIX_Mixer](MIX_Mixer) *) Returns the mixer associated with the track, or
NULL on error; call SDL_GetError() for more information.

## Remarks

This is the mixer pointer that was passed to
[MIX_CreateTrack](MIX_CreateTrack)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

