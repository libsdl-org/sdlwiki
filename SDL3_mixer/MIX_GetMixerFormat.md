###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetMixerFormat

Get the audio format a mixer is generating.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_GetMixerFormat(MIX_Mixer *mixer, SDL_AudioSpec *spec);
```

## Function Parameters

|                          |           |                                        |
| ------------------------ | --------- | -------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to query.                    |
| SDL_AudioSpec *          | **spec**  | where to store the mixer audio format. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Generally you don't need this information, as SDL_mixer will convert data
as necessary between inputs you provide and its output format, but it might
be useful if trying to match your inputs to reduce conversion and
resampling costs.

For mixers created with [MIX_CreateMixerDevice](MIX_CreateMixerDevice)(),
this is the format of the audio device (and may change later if the device
itself changes; SDL_mixer will seamlessly handle this change internally,
though).

For mixers created with [MIX_CreateMixer](MIX_CreateMixer)(), this is the
format that [MIX_Generate](MIX_Generate)() will produce, as requested at
create time, and does not change.

Note that internally, SDL_mixer will work in SDL_AUDIO_F32 format before
outputting the format specified here, so it would be more efficient to
match input data to that, not the final output format.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

