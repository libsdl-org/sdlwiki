###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PauseAllTracks

Pause all currently-playing tracks.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_PauseAllTracks(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                                         |
| ------------------------ | --------- | --------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer on which to pause all tracks. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

A paused track is not considered "stopped," so its
[MIX_TrackStoppedCallback](MIX_TrackStoppedCallback) will not fire if
paused, but it won't change state by default, generate audio, or generally
make progress, until it is resumed.

This function makes all tracks on the specified mixer that are currently
playing move to a paused state. They can later be resumed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_ResumeTrack](MIX_ResumeTrack)
- [MIX_ResumeAllTracks](MIX_ResumeAllTracks)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

