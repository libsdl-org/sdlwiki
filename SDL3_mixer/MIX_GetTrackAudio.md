###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackAudio

Query the [MIX_Audio](MIX_Audio) assigned to a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Audio * MIX_GetTrackAudio(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

([MIX_Audio](MIX_Audio) *) Returns a [MIX_Audio](MIX_Audio) if available,
NULL if not.

## Remarks

This returns the [MIX_Audio](MIX_Audio) object currently assigned to
`track` through a call to [MIX_SetTrackAudio](MIX_SetTrackAudio)(). If
there is none assigned, or the track has an input that isn't a
[MIX_Audio](MIX_Audio) (such as an SDL_AudioStream or SDL_IOStream), this
will return NULL.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns NULL, but there is no mechanism to distinguish errors
from tracks without a valid input.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackAudioStream](MIX_GetTrackAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

