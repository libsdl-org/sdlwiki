###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PlayAudioDevice

Use this function to play audio on a specified device.

## Syntax

```c
int SDL_PlayAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                 |
| ----------- | --------------------------------------------------------------- |
| **dev**     | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Newly-opened audio devices start in the paused state, so you must call this
function after opening the specified audio device to start playing sound.
This allows you to safely initialize data for your callback function after
opening the audio device. Silence will be written to the audio device while
paused, and the audio callback is guaranteed to not be called. Pausing one
device does not prevent other unpaused devices from running their
callbacks.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockAudioDevice](SDL_LockAudioDevice)
* [SDL_PauseAudioDevice](SDL_PauseAudioDevice)

----
[CategoryAPI](CategoryAPI)

