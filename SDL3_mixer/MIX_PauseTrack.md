###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PauseTrack

Pause a currently-playing track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_PauseTrack(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to pause. |

## Return Value

(bool) Returns true if the track has paused, false on error; call
SDL_GetError() for details.

## Remarks

A paused track is not considered "stopped," so its
[MIX_TrackStoppedCallback](MIX_TrackStoppedCallback) will not fire if
paused, but it won't change state by default, generate audio, or generally
make progress, until it is resumed.

It is legal to pause a track that's in any state (playing, already paused,
or stopped). Unless the track is currently playing, pausing does nothing,
and returns true. A false return is only used to signal errors here (such
as [MIX_Init](MIX_Init) not being called or `track` being NULL).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_ResumeTrack](MIX_ResumeTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

