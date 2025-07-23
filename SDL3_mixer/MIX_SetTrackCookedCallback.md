###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackCookedCallback

Set a callback that fires when the mixer has transformed a track's audio.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackCookedCallback(MIX_Track *track, MIX_TrackMixCallback cb, void *userdata);
```

## Function Parameters

|                                              |              |                                                                      |
| -------------------------------------------- | ------------ | -------------------------------------------------------------------- |
| [MIX_Track](MIX_Track) *                     | **track**    | the track to assign this callback to.                                |
| [MIX_TrackMixCallback](MIX_TrackMixCallback) | **cb**       | the function to call when the track mixes. May be NULL.              |
| void *                                       | **userdata** | an opaque pointer provided to the callback for its own personal use. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

As a track needs to mix more data, it pulls from its input (a
[MIX_Audio](MIX_Audio), an SDL_AudioStream, etc). This input might be a
compressed file format, like MP3, so a little more data is uncompressed
from it.

Once the track has PCM data to start operating on, and its raw callback has
completed, it will begin to transform the audio: gain, fading, frequency
ratio, 3D positioning, etc.

A callback can be fired after all these transformations, but before the
transformed data is mixed into other tracks. This lets an app view the data
at the last moment that it is still a part of this track. It can also
change the data in any way it pleases during this callback, and the mixer
will continue as if this data came directly from the input.

Each track has its own unique cooked callback.

Passing a NULL callback here is legal; it disables this track's callback.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TrackMixCallback](MIX_TrackMixCallback)
- [MIX_SetTrackRawCallback](MIX_SetTrackRawCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

