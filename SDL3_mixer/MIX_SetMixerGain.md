###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_SetMixerGain

Set a mixer's master gain control.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_SetMixerGain(MIX_Mixer *mixer, float gain);
```

## Function Parameters

|                          |           |                      |
| ------------------------ | --------- | -------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to adjust. |
| float                    | **gain**  | the new gain value.  |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Each mixer has a master gain, to adjust the volume of the entire mix. Each
sample passing through the pipeline is modulated by this gain value. A gain
of zero will generate silence, 1.0f will not change the mixed volume, and
larger than 1.0f will increase the volume. Negative values are illegal.
There is no maximum gain specified, but this can quickly get extremely
loud, so please be careful with this setting.

A mixer's master gain defaults to 1.0f.

This value can be changed at any time to adjust the future mix.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetMixerGain](MIX_GetMixerGain)
- [MIX_SetTrackGain](MIX_SetTrackGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

