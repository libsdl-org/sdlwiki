###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_CreateMixerDevice

Create a mixer that plays sound directly to an audio device.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_Mixer * MIX_CreateMixerDevice(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);
```

## Function Parameters

|                       |           |                                                                                        |
| --------------------- | --------- | -------------------------------------------------------------------------------------- |
| SDL_AudioDeviceID     | **devid** | the device to open for playback, or SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK for the default. |
| const SDL_AudioSpec * | **spec**  | the audio format to request from the device. May be NULL.                              |

## Return Value

([MIX_Mixer](MIX_Mixer) *) Returns a mixer that can be used to play audio,
or NULL on failure; call SDL_GetError() for more information.

## Remarks

This is usually the function you want, vs
[MIX_CreateMixer](MIX_CreateMixer)().

You can choose a specific device ID to open, following SDL's usual rules,
but often the correct choice is to specify
SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK and let SDL figure out what device to use
(and seamlessly transition you to new hardware if the default changes).

Only playback devices make sense here. Attempting to open a recording
device will fail.

This will call SDL_Init(SDL_INIT_AUDIO) internally; it's safe to call
SDL_Init() before this call, too, if you intend to enumerate audio devices
to choose one to open here.

An audio format can be requested, and the system will try to set the
hardware to those specifications, or as close as possible, but this is just
a hint. SDL_mixer will handle all data conversion behind the scenes in any
case, and specifying a NULL spec is a reasonable choice. The best reason to
specify a format is because you know all your data is in that format and it
might save some unnecessary CPU time on conversion.

The actual device format chosen is available through
[MIX_GetMixerFormat](MIX_GetMixerFormat)().

Once a mixer is created, next steps are usually to load audio (through
[MIX_LoadAudio](MIX_LoadAudio)() and friends), create a track
([MIX_CreateTrack](MIX_CreateTrack)()), and play that audio through that
track.

When done with the mixer, it can be destroyed with
[MIX_DestroyMixer](MIX_DestroyMixer)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_CreateMixer](MIX_CreateMixer)
- [MIX_DestroyMixer](MIX_DestroyMixer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

