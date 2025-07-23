###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_StopTag

Halt all tracks with a specific tag, possibly fading out over time.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_StopTag(MIX_Mixer *mixer, const char *tag, Sint64 fade_out_ms);
```

## Function Parameters

|                          |                 |                                                                                                  |
| ------------------------ | --------------- | ------------------------------------------------------------------------------------------------ |
| [MIX_Mixer](MIX_Mixer) * | **mixer**       | the mixer on which to stop tracks.                                                               |
| const char *             | **tag**         | the tag to use when searching for tracks.                                                        |
| Sint64                   | **fade_out_ms** | the number of milliseconds to spend fading out to silence before halting. 0 to stop immediately. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

If `fade_out_ms` is > 0, the tracks do not stop mixing immediately, but
rather fades to silence over that many milliseconds before stopping. Note
that this is different than [MIX_StopTrack](MIX_StopTrack)(), which wants
sample frames; this function takes milliseconds because different tracks
might have different sample rates.

If a track ends normally while the fade-out is still in progress, the audio
stops there; the fade is not adjusted to be shorter if it will last longer
than the audio remaining.

Once a track has completed any fadeout and come to a stop, it will call its
[MIX_TrackStoppedCallback](MIX_TrackStoppedCallback), if any. It is legal
to assign the track a new input and/or restart it during this callback.
This function does not prevent new play requests from being made.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_StopTrack](MIX_StopTrack)
- [MIX_TagTrack](MIX_TagTrack)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

