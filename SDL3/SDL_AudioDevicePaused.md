# SDL_AudioDevicePaused

Use this function to query if an audio device is paused.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_AudioDevicePaused(SDL_AudioDeviceID dev);
```

## Function Parameters

|                                        |         |                                                                  |
| -------------------------------------- | ------- | ---------------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev** | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)(). |

## Return Value

(bool) Returns true if device is valid and paused, false otherwise.

## Remarks

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow.

Physical devices can not be paused or unpaused, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.
Physical and invalid device IDs will report themselves as unpaused here.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PauseAudioDevice](SDL_PauseAudioDevice)
- [SDL_ResumeAudioDevice](SDL_ResumeAudioDevice)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

