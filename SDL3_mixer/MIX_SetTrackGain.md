###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackGain

Set a track's gain control.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackGain(MIX_Track *track, float gain);
```

## Function Parameters

|                          |           |                      |
| ------------------------ | --------- | -------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to adjust. |
| float                    | **gain**  | the new gain value.  |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Each track has its own gain, to adjust its overall volume. Each sample from
this track is modulated by this gain value. A gain of zero will generate
silence, 1.0f will not change the mixed volume, and larger than 1.0f will
increase the volume. Negative values are illegal. There is no maximum gain
specified, but this can quickly get extremely loud, so please be careful
with this setting.

A track's gain defaults to 1.0f.

This value can be changed at any time to adjust the future mix.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackGain](MIX_GetTrackGain)
- [MIX_SetMasterGain](MIX_SetMasterGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

