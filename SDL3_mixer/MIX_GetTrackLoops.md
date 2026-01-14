###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackLoops

Query how many loops remain for a given track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int MIX_GetTrackLoops(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(int) Returns the number of pending loops, zero if not looping, and -1 if
looping infinitely.

## Remarks

This returns the number of loops still pending; if a track will eventually
complete and loop to play again one more time, this will return 1. If a
track _was_ looping but is on its final iteration of the loop (will stop
when this iteration completes), this will return zero.

A track that is looping infinitely will return -1. This value does not
report an error in this case.

A track that is stopped (not playing and not paused) will have zero loops
remaining.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns zero, but there is no mechanism to distinguish errors
from non-looping tracks.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

