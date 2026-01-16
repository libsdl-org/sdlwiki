###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetMixerFrequencyRatio

Set a mixer's master frequency ratio.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetMixerFrequencyRatio(MIX_Mixer *mixer, float ratio);
```

## Function Parameters

|                          |           |                                                        |
| ------------------------ | --------- | ------------------------------------------------------ |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to adjust.                                   |
| float                    | **ratio** | the frequency ratio. Must be between 0.01f and 100.0f. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Each mixer has a master frequency ratio, that affects the entire mix. This
can cause the final output to change speed and pitch. A value greater than
1.0f will play the audio faster, and at a higher pitch. A value less than
1.0f will play the audio slower, and at a lower pitch. 1.0f is normal
speed.

Each track _also_ has a frequency ratio; it will be applied when mixing
that track's audio regardless of the master setting. The master setting
affects the final output after all mixing has been completed.

A mixer's master frequency ratio defaults to 1.0f.

This value can be changed at any time to adjust the future mix.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetMixerFrequencyRatio](MIX_GetMixerFrequencyRatio)
- [MIX_SetTrackFrequencyRatio](MIX_SetTrackFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

