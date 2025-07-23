###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackAudioStream

Query the SDL_AudioStream assigned to a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
SDL_AudioStream * MIX_GetTrackAudioStream(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(SDL_AudioStream *) Returns an SDL_AudioStream if available, NULL if not.

## Remarks

This returns the SDL_AudioStream object currently assigned to `track`
through a call to [MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)(). If
there is none assigned, or the track has an input that isn't an
SDL_AudioStream (such as a [MIX_Audio](MIX_Audio) or SDL_IOStream), this
will return NULL.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns NULL, but there is no mechanism to distinguish errors
from tracks without a valid input.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackAudio](MIX_GetTrackAudio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

