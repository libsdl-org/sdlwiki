###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackPlaybackPosition

Seek a playing track to a new position in its input.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackPlaybackPosition(MIX_Track *track, Sint64 frames);
```

## Function Parameters

|                          |            |                                       |
| ------------------------ | ---------- | ------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**  | the track to change.                  |
| Sint64                   | **frames** | the sample frame position to seek to. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

(Not to be confused with
[MIX_SetTrack3DPosition](MIX_SetTrack3DPosition)(), which is positioning of
the track in 3D space, not the playback position of its audio data.)

On a playing track, the next time the mixer runs, it will start mixing from
the new position.

Position is defined in _sample frames_ of decoded audio, not units of time,
so that sample-perfect mixing can be achieved. To instead operate in units
of time, use [MIX_TrackMSToFrames](MIX_TrackMSToFrames)() to get the
approximate sample frames for a given tick.

This function requires an input that can seek (so it can not be used if the
input was set with [MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)()),
and a audio file format that allows seeking. SDL_mixer's decoders for some
file formats do not offer seeking, or can only seek to times, not exact
sample frames, in which case the final position may be off by some amount
of sample frames. Please check your audio data and file bug reports if
appropriate.

It's legal to call this function on a track that is stopped, but a future
call to [MIX_PlayTrack](MIX_PlayTrack)() will reset the start position
anyhow. Paused tracks will resume at the new input position.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackPlaybackPosition](MIX_GetTrackPlaybackPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

