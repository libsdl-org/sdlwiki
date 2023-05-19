###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PauseAudioDevice

Use this function to pause audio playback on a specified device.

## Syntax

```c
int SDL_PauseAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                 |
| ----------- | --------------------------------------------------------------- |
| **dev**     | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function pauses the audio callback processing for a given device.
Silence will be written to the audio device while paused, and the audio
callback is guaranteed to not be called. Pausing one device does not
prevent other unpaused devices from running their callbacks.

If you just need to protect a few variables from race conditions vs your
callback, you shouldn't pause the audio device, as it will lead to dropouts
in the audio playback. Instead, you should use
[SDL_LockAudioDevice](SDL_LockAudioDevice)().

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_AudioDeviceID devid;
SDL_PauseAudioDevice(devid);  // audio callback is stopped when this returns.
SDL_Delay(5000);  // audio device plays silence for 5 seconds
SDL_PlayAudioDevice(devid);  // audio callback starts running again.
```

## Related Functions

* [SDL_LockAudioDevice](SDL_LockAudioDevice)
* [SDL_PlayAudioDevice](SDL_PlayAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAudio](CategoryAudio)


