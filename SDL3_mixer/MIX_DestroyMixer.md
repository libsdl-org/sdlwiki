###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_DestroyMixer

Free a mixer.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_DestroyMixer(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                       |
| ------------------------ | --------- | --------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to destroy. |

## Remarks

If this mixer was created with
[MIX_CreateMixerDevice](MIX_CreateMixerDevice)(), this function will also
close the audio device and call SDL_QuitSubSystem(SDL_INIT_AUDIO).

Any [MIX_Group](MIX_Group) or [MIX_Track](MIX_Track) created for this mixer
will also be destroyed. Do not access them again or attempt to destroy them
after the device is destroyed. [MIX_Audio](MIX_Audio) objects will not be
destroyed, since they can be shared between mixers (but those will all be
destroyed during [MIX_Quit](MIX_Quit)()).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_CreateMixerDevice](MIX_CreateMixerDevice)
- [MIX_CreateMixer](MIX_CreateMixer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

