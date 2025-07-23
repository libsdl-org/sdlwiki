###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_TrackPaused

Query if a track is currently paused.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_TrackPaused(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(bool) Returns true if paused, false otherwise.

## Remarks

If this returns true, the track is not currently contributing to the
mixer's output but will when resumed (it's "paused"). It is not playing nor
stopped.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns false, but there is no mechanism to distinguish errors
from non-playing tracks.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PlayTrack](MIX_PlayTrack)
- [MIX_PauseTrack](MIX_PauseTrack)
- [MIX_ResumeTrack](MIX_ResumeTrack)
- [MIX_StopTrack](MIX_StopTrack)
- [MIX_TrackPlaying](MIX_TrackPlaying)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

