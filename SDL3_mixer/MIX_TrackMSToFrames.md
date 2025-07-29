###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_TrackMSToFrames

Convert milliseconds to sample frames for a track's current format.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_TrackMSToFrames(MIX_Track *track, Sint64 ms);
```

## Function Parameters

|                          |           |                                                              |
| ------------------------ | --------- | ------------------------------------------------------------ |
| [MIX_Track](MIX_Track) * | **track** | the track to query.                                          |
| Sint64                   | **ms**    | the milliseconds to convert to track-specific sample frames. |

## Return Value

(Sint64) Returns Converted number of sample frames, or -1 for errors/no
input; call SDL_GetError() for details.

## Remarks

This calculates time based on the track's current input format, which can
change when its input does, and also if that input changes formats
mid-stream (for example, if decoding a file that is two MP3s concatenated
together).

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns -1. If the track has no input, this returns -1. If `ms`
is < 0, this returns -1.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TrackFramesToMS](MIX_TrackFramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

