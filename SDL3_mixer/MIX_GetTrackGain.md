###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackGain

Get a track's gain control.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
float MIX_GetTrackGain(MIX_Track *track);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Track](MIX_Track) * | **track** | the track to query. |

## Return Value

(float) Returns the track's current gain.

## Remarks

This returns the last value set through
[MIX_SetTrackGain](MIX_SetTrackGain)(), or 1.0f if no value has ever been
explicitly set.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrackGain](MIX_SetTrackGain)
- [MIX_GetMasterGain](MIX_GetMasterGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

