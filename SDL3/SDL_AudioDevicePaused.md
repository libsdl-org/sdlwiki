###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AudioDevicePaused

Use this function to query if an audio device is paused.

## Syntax

```c
SDL_bool SDL_AudioDevicePaused(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                 |
| ----------- | --------------------------------------------------------------- |
| **dev**     | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if device is valid and paused,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow.

Physical devices can not be paused or unpaused, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.
Physical and invalid device IDs will report themselves as unpaused here.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PauseAudioDevice](SDL_PauseAudioDevice)
* [SDL_ResumeAudioDevice](SDL_ResumeAudioDevice)

----
[CategoryAPI](CategoryAPI)

