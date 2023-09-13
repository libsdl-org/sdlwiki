###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ResumeAudioDevice

Use this function to unpause audio playback on a specified device.

## Syntax

```c
int SDL_ResumeAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                 |
| ----------- | --------------------------------------------------------------- |
| **dev**     | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unpauses audio processing for a given device that has
previously been paused with [SDL_PauseAudioDevice](SDL_PauseAudioDevice)().
Once unpaused, any bound audio streams will begin to progress again, and
audio can be generated.

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow. Unpausing an unpaused
device is a legal no-op.

Physical devices can not be paused or unpaused, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AudioDevicePaused](SDL_AudioDevicePaused)
* [SDL_PauseAudioDevice](SDL_PauseAudioDevice)

----
[CategoryAPI](CategoryAPI)

