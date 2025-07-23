###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_PlayTag

Start (or restart) mixing all tracks with a specific tag for playback.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_PlayTag(MIX_Mixer *mixer, const char *tag, SDL_PropertiesID options);
```

## Function Parameters

|                          |             |                                                        |
| ------------------------ | ----------- | ------------------------------------------------------ |
| [MIX_Mixer](MIX_Mixer) * | **mixer**   | the mixer on which to look for tagged tracks.          |
| const char *             | **tag**     | the tag to use when searching for tracks.              |
| SDL_PropertiesID         | **options** | the set of options that will be applied to each track. |

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

This function follows all the same rules as
[MIX_PlayTrack](MIX_PlayTrack)(); please refer to its documentation for the
details. Unlike that function, [MIX_PlayTag](MIX_PlayTag)() operates on
multiple tracks at once that have the specified tag applied, via
[MIX_TagTrack](MIX_TagTrack)().

If all of your tagged tracks have different sample rates, it would make
sense to use the `*_MILLISECONDS_NUMBER` properties in your `options`,
instead of `*_FRAMES_NUMBER`, and let SDL_mixer figure out how to apply it
to each track.

This function returns true if all tagged tracks are started (or restarted).
If any track fails, this function returns false, but all tracks that could
start will still be started even when this function reports failure.

From the point of view of the mixing process, all tracks that successfully
(re)start will do so at the exact same moment.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_PlayTrack](MIX_PlayTrack)
- [MIX_TagTrack](MIX_TagTrack)
- [MIX_StopTrack](MIX_StopTrack)
- [MIX_PauseTrack](MIX_PauseTrack)
- [MIX_TrackPlaying](MIX_TrackPlaying)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

