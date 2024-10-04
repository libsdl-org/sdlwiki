###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PauseAudioDevice

Use this function to pause audio playback on a specified device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_PauseAudioDevice(SDL_AudioDeviceID dev);
```

## Function Parameters

|                                        |         |                                                                  |
| -------------------------------------- | ------- | ---------------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev** | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)(). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function pauses audio processing for a given device. Any bound audio
streams will not progress, and no audio will be generated. Pausing one
device does not prevent other unpaused devices from running.

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow. Pausing a paused device is
a legal no-op.

Pausing a device can be useful to halt all audio without unbinding all the
audio streams. This might be useful while a game is paused, or a level is
loading, etc.

Physical devices can not be paused or unpaused, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ResumeAudioDevice](SDL_ResumeAudioDevice)
- [SDL_AudioDevicePaused](SDL_AudioDevicePaused)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

