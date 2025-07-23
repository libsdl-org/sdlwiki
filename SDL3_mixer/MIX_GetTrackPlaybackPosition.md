###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackPlaybackPosition

Get the current input position of a playing track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_GetTrackPlaybackPosition(MIX_Track *track);
```

## Function Parameters

|                          |           |                      |
| ------------------------ | --------- | -------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to change. |

## Return Value

(Sint64) Returns the track's current sample frame position, or -1 on error;
call SDL_GetError() for details.

## Remarks

(Not to be confused with
[MIX_GetTrack3DPosition](MIX_GetTrack3DPosition)(), which is positioning of
the track in 3D space, not the playback position of its audio data.)

Position is defined in _sample frames_ of decoded audio, not units of time,
so that sample-perfect mixing can be achieved. To instead operate in units
of time, use [MIX_TrackFramesToMS](MIX_TrackFramesToMS)() to convert the
return value to milliseconds.

Stopped and paused tracks will report the position when they halted.
Playing tracks will report the current position, which will change over
time.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrackPlaybackPosition](MIX_SetTrackPlaybackPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

