###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetMixerProperties

Get the properties associated with a mixer.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
SDL_PropertiesID MIX_GetMixerProperties(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Remarks

The following read-only properties are provided by SDL_mixer:

- [`MIX_PROP_MIXER_DEVICE_NUMBER`](MIX_PROP_MIXER_DEVICE_NUMBER): the
  SDL_AudioDeviceID that this mixer has opened for playback. This will be
  zero (no device) if the mixer was created with Mix_CreateMixer() instead
  of Mix_CreateMixerDevice().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

