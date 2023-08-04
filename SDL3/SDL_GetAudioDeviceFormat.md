###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioDeviceFormat

Get the current audio format of a specific audio device.

## Syntax

```c
int SDL_GetAudioDeviceFormat(SDL_AudioDeviceID devid, SDL_AudioSpec *spec);

```

## Function Parameters

|               |                                                |
| ------------- | ---------------------------------------------- |
| **devid**     | the instance ID of the device to query.        |
| **spec**      | On return, will be filled with device details. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

For an opened device, this will report the format the device is currently
using. If the device isn't yet opened, this will report the device's
preferred format (or a reasonable default if this can't be determined).

You may also specify
[SDL_AUDIO_DEVICE_DEFAULT_OUTPUT](SDL_AUDIO_DEVICE_DEFAULT_OUTPUT) or
[SDL_AUDIO_DEVICE_DEFAULT_CAPTURE](SDL_AUDIO_DEVICE_DEFAULT_CAPTURE) here,
which is useful for getting a reasonable recommendation before opening the
system-recommended default device.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

