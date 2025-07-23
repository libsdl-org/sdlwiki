###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_StopTrack

Halt a currently-playing track, possibly fading out over time.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_StopTrack(MIX_Track *track, Sint64 fade_out_frames);
```

## Function Parameters

|                          |                     |                                                                                                   |
| ------------------------ | ------------------- | ------------------------------------------------------------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**           | the track to halt.                                                                                |
| Sint64                   | **fade_out_frames** | the number of sample frames to spend fading out to silence before halting. 0 to stop immediately. |

## Return Value

(bool) Returns true if the track has stopped, false on error; call
SDL_GetError() for details.

## Remarks

If `fade_out_frames` is > 0, the track does not stop mixing immediately,
but rather fades to silence over that many sample frames before stopping.
Sample frames are specific to the input assigned to the track, to allow for
sample-perfect mixing. [MIX_TrackMSToFrames](MIX_TrackMSToFrames)() can be
used to convert milliseconds to an appropriate value here.

If the track ends normally while the fade-out is still in progress, the
audio stops there; the fade is not adjusted to be shorter if it will last
longer than the audio remaining.

Once a track has completed any fadeout and come to a stop, it will call its
[MIX_TrackStoppedCallback](MIX_TrackStoppedCallback), if any. It is legal
to assign the track a new input and/or restart it during this callback.

It is legal to halt a track that's already stopped. It does nothing, and
returns true.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PlayTrack](MIX_PlayTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

