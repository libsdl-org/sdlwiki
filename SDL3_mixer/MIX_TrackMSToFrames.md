###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_TrackMSToFrames

Convert milliseconds to sample frames for a track's current format.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Uint64 MIX_TrackMSToFrames(MIX_Track *track, Uint64 ms);
```

## Function Parameters

|                          |           |                                                              |
| ------------------------ | --------- | ------------------------------------------------------------ |
| [MIX_Track](MIX_Track) * | **track** | the track to query.                                          |
| Uint64                   | **ms**    | the milliseconds to convert to track-specific sample frames. |

## Return Value

(Uint64) Returns Converted number of sample frames, or zero for errors/no
input.

## Remarks

This calculates time based on the track's current input format, which can
change when its input does, and also if that input changes formats
mid-stream (for example, if decoding a file that is two MP3s concatenated
together).

If the track has no input, this returns 0.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns 0, but there is no mechanism to distinguish errors from
tracks without a valid input.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TrackFramesToMS](MIX_TrackFramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

