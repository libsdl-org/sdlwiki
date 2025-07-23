###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackStereo

Force a track to stereo output, with optionally left/right panning.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackStereo(MIX_Track *track, const MIX_StereoGains *gains);
```

## Function Parameters

|                                            |           |                                                           |
| ------------------------------------------ | --------- | --------------------------------------------------------- |
| [MIX_Track](MIX_Track) *                   | **track** | the track to adjust.                                      |
| const [MIX_StereoGains](MIX_StereoGains) * | **gains** | the per-channel gains, or NULL to disable spatialization. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This will cause the output of the track to convert to stereo, and then mix
it only onto the Front Left and Front Right speakers, regardless of the
speaker configuration. The left and right channels are modulated by
`gains`, which can be used to produce panning effects. This function may be
called to adjust the gains at any time.

If `gains` is not NULL, this track will be switched into forced-stereo
mode. If `gains` is NULL, this will disable spatialization (both the
forced-stereo mode of this function and full 3D spatialization of
[MIX_SetTrack3DPosition](MIX_SetTrack3DPosition)()).

Negative gains are clamped to zero; there is no clamp for maximum, so one
could set the value > 1.0f to make a channel louder.

The track's 3D position, reported by
[MIX_GetTrack3DPosition](MIX_GetTrack3DPosition)(), will be reset to (0, 0,
0).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrack3DPosition](MIX_SetTrack3DPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

