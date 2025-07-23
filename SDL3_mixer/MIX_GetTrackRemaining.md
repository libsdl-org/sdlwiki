###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackRemaining

Return the number of sample frames remaining to be mixed in a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_GetTrackRemaining(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(Sint64) Returns the total sample frames still to be mixed, or -1 if
unknown.

## Remarks

If the track is playing or paused, and its total duration is known, this
will report how much audio is left to mix. If the track is playing, future
calls to this function will report different values.

Remaining audio is defined in _sample frames_ of decoded audio, not units
of time, so that sample-perfect mixing can be achieved. To instead operate
in units of time, use [MIX_TrackFramesToMS](MIX_TrackFramesToMS)() to
convert the return value to milliseconds.

This function does not take into account fade-outs or looping, just the
current mixing position vs the duration of the track.

If the duration of the track isn't known, or `track` is NULL, this function
returns -1. A stopped track reports 0.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

