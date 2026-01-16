###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetMasterFrequencyRatio

Get a mixer's master frequency ratio.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
float MIX_GetMasterFrequencyRatio(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to query. |

## Return Value

(float) Returns the mixer's current master frequency ratio.

## Remarks

This returns the last value set through
[MIX_SetMasterFrequencyRatio](MIX_SetMasterFrequencyRatio)(), or 1.0f if no
value has ever been explicitly set.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetMasterFrequencyRatio](MIX_SetMasterFrequencyRatio)
- [MIX_GetTrackFrequencyRatio](MIX_GetTrackFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

