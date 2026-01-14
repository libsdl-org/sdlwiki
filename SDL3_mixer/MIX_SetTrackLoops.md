###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackLoops

Change the number of times a currently-playing track will loop.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackLoops(MIX_Track *track, int num_loops);
```

## Function Parameters

|                          |               |                                                                              |
| ------------------------ | ------------- | ---------------------------------------------------------------------------- |
| [MIX_Track](MIX_Track) * | **track**     | the track to configure.                                                      |
| int                      | **num_loops** | new number of times to loop. Zero to disable looping, -1 to loop infinitely. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

This replaces any previously-set remaining loops. A value of 1 will loop to
the start of playback one time. Zero will not loop at all. A value of -1
requests infinite loops. If the input is not seekable and `num_loops` isn't
zero, this function will report success but the track will stop at the
point it should loop.

The new loop count replaces any previous state, even if the track has
already looped.

This has no effect on a track that is stopped, or rather, starting a
stopped track later will set a new loop count, replacing this value.
Stopped tracks can specify a loop count while starting via
[MIX_PROP_PLAY_LOOPS_NUMBER](MIX_PROP_PLAY_LOOPS_NUMBER). This function is
intended to alter that count in the middle of playback.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackLoops](MIX_GetTrackLoops)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

