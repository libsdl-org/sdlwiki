###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetTrackFrequencyRatio

Change the frequency ratio of a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetTrackFrequencyRatio(MIX_Track *track, float ratio);
```

## Function Parameters

|                          |           |                                                        |
| ------------------------ | --------- | ------------------------------------------------------ |
| [MIX_Track](MIX_Track) * | **track** | the track on which to change the frequency ratio.      |
| float                    | **ratio** | the frequency ratio. Must be between 0.01f and 100.0f. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The frequency ratio is used to adjust the rate at which audio data is
consumed. Changing this effectively modifies the speed and pitch of the
track's audio. A value greater than 1.0f will play the audio faster, and at
a higher pitch. A value less than 1.0f will play the audio slower, and at a
lower pitch. 1.0f is normal speed.

The default value is 1.0f.

This value can be changed at any time to adjust the future mix.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackFrequencyRatio](MIX_GetTrackFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

