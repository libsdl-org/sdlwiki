###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackRawCallback

Set a callback that fires when a [MIX_Track](MIX_Track) has initial decoded audio.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackRawCallback(MIX_Track *track, MIX_TrackMixCallback cb, void *userdata);
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

Once the track has PCM data to start operating on, it can fire a callback
before _any_ changes to the raw PCM input have happened. This lets an app
view the data before it has gone through transformations such as gain, 3D
positioning, fading, etc. It can also change the data in any way it pleases
during this callback, and the mixer will continue as if this data came
directly from the input.

Each track has its own unique raw callback.

Passing a NULL callback here is legal; it disables this track's callback.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TrackMixCallback](MIX_TrackMixCallback)
- [MIX_SetTrackCookedCallback](MIX_SetTrackCookedCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

