###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackStoppedCallback

Set a callback that fires when a [MIX_Track](MIX_Track) is stopped.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackStoppedCallback(MIX_Track *track, MIX_TrackStoppedCallback cb, void *userdata);
```

## Function Parameters

|                                                      |              |                                                                      |
| ---------------------------------------------------- | ------------ | -------------------------------------------------------------------- |
| [MIX_Track](MIX_Track) *                             | **track**    | the track to assign this callback to.                                |
| [MIX_TrackStoppedCallback](MIX_TrackStoppedCallback) | **cb**       | the function to call when the track stops. May be NULL.              |
| void *                                               | **userdata** | an opaque pointer provided to the callback for its own personal use. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

When a track completes playback, either because it ran out of data to mix
(and all loops were completed as well), or it was explicitly stopped by the
app, it will fire the callback specified here.

Each track has its own unique callback.

Passing a NULL callback here is legal; it disables this track's callback.

Pausing a track will not fire the callback, nor will the callback fire on a
playing track that is being destroyed.

It is legal to adjust the track, including changing its input and
restarting it. If this is done because it ran out of data in the middle of
mixing, the mixer will start mixing the new track state in its current run
without any gap in the audio.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_TrackStoppedCallback](MIX_TrackStoppedCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

