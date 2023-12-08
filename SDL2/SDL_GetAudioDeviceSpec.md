###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetAudioDeviceSpec

Get the preferred audio format of a specific audio device.

## Syntax

```c
int SDL_GetAudioDeviceSpec(int index,
                           int iscapture,
                           SDL_AudioSpec *spec);

```

## Function Parameters

|                   |                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| **index**         | the index of the audio device; valid values range from 0 to [SDL_GetNumAudioDevices](SDL_GetNumAudioDevices.md)() - 1 |
| **iscapture**     | non-zero to query the list of recording devices, zero to query the list of output devices.                         |
| **spec**          | The [SDL_AudioSpec](SDL_AudioSpec.md) to be initialized by this function.                                             |

## Return Value

Returns 0 on success, nonzero on error

## Remarks

This function is only valid after a successfully initializing the audio
subsystem. The values returned by this function reflect the latest call to
[SDL_GetNumAudioDevices](SDL_GetNumAudioDevices.md)(); re-call that function
to redetect available hardware.

`spec` will be filled with the sample rate, sample format, and channel
count.

## Version

This function is available since SDL 2.0.16.

## Related Functions

* [SDL_GetNumAudioDevices](SDL_GetNumAudioDevices.md)
* [SDL_GetDefaultAudioInfo](SDL_GetDefaultAudioInfo.md)

----
[CategoryAPI](CategoryAPI.md)
