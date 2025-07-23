###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrack3DPosition

Set a track's position in 3D space.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrack3DPosition(MIX_Track *track, const MIX_Point3D *position);
```

## Function Parameters

|                                    |              |                                                 |
| ---------------------------------- | ------------ | ----------------------------------------------- |
| [MIX_Track](MIX_Track) *           | **track**    | the track for which to set 3D position.         |
| const [MIX_Point3D](MIX_Point3D) * | **position** | the new 3D position for the track. May be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

(Please note that SDL_mixer is not intended to be a extremely powerful 3D
API. It lacks 3D features that other APIs like OpenAL offer: there's no
doppler effect, distance models, rolloff, etc. This is meant to be Good
Enough for games that can use some positional sounds and can even take
advantage of surround-sound configurations.)

If `position` is not NULL, this track will be switched into 3D positional
mode. If `position` is NULL, this will disable positional mixing (both the
full 3D spatialization of this function and forced-stereo mode of
[MIX_SetTrackStereo](MIX_SetTrackStereo)()).

In 3D positional mode, SDL_mixer will mix this track as if it were
positioned in 3D space, including distance attenuation (quieter as it gets
further from the listener) and spatialization (positioned on the correct
speakers to suggest direction, either with stereo outputs or full surround
sound).

For a mono speaker output, spatialization is effectively disabled but
distance attenuation will still work, which is all you can really do with a
single speaker.

The coordinate system operates like OpenGL or OpenAL: a "right-handed"
coordinate system. See [MIX_Point3D](MIX_Point3D) for the details.

The listener is always at coordinate (0,0,0) and can't be changed.

The track's input will be converted to mono (1 channel) so it can be
rendered across the correct speakers.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrack3DPosition](MIX_GetTrack3DPosition)
- [MIX_SetTrackStereo](MIX_SetTrackStereo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

