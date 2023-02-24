###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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
| **index**         | the index of the audio device; valid values range from 0 to [SDL_GetNumAudioDevices](SDL_GetNumAudioDevices)() - 1 |
| **iscapture**     | non-zero to query the list of recording devices, zero to query the list of output devices.                         |
| **spec**          | The [SDL_AudioSpec](SDL_AudioSpec) to be initialized by this function.                                             |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function is only valid after a successfully initializing the audio
subsystem. The values returned by this function reflect the latest call to
[SDL_GetNumAudioDevices](SDL_GetNumAudioDevices)(); re-call that function
to redetect available hardware.

`spec` will be filled with the sample rate, sample format, and channel
count.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumAudioDevices](SDL_GetNumAudioDevices)
* [SDL_GetDefaultAudioInfo](SDL_GetDefaultAudioInfo)

----
[CategoryAPI](CategoryAPI)

