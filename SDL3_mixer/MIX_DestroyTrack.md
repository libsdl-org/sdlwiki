###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_DestroyTrack

Destroy the specified track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_DestroyTrack(MIX_Track *track);
```

## Function Parameters

|                          |           |                       |
| ------------------------ | --------- | --------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to destroy. |

## Remarks

If the track is currently playing, it will be stopped immediately, without
any fadeout. If there is a callback set through
[MIX_SetTrackStoppedCallback](MIX_SetTrackStoppedCallback)(), it will _not_
be called.

If the mixer is currently mixing in another thread, this will block until
it finishes.

Destroying a NULL [MIX_Track](MIX_Track) is a legal no-op.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

