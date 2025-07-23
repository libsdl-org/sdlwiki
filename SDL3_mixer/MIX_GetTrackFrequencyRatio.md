###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetTrackFrequencyRatio

Query the frequency ratio of a track.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
float MIX_GetTrackFrequencyRatio(MIX_Track *track);
```

## Function Parameters

|                          |           |                                                  |
| ------------------------ | --------- | ------------------------------------------------ |
| [MIX_Track](MIX_Track) * | **track** | the track on which to query the frequency ratio. |

## Return Value

(float) Returns the current frequency ratio, or 0.0f on failure; call
SDL_GetError() for more information.

## Remarks

The frequency ratio is used to adjust the rate at which audio data is
consumed. Changing this effectively modifies the speed and pitch of the
track's audio. A value greater than 1.0f will play the audio faster, and at
a higher pitch. A value less than 1.0f will play the audio slower, and at a
lower pitch. 1.0f is normal speed.

The default value is 1.0f.

On various errors ([MIX_Init](MIX_Init)() was not called, the track is
NULL), this returns 0.0f. Since this is not a valid value to set, this can
be seen as an error state.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetTrackFrequencyRatio](MIX_GetTrackFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

