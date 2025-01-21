###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAudioDeviceName

Get the human-readable name of a specific audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
const char * SDL_GetAudioDeviceName(SDL_AudioDeviceID devid);
```

## Function Parameters

|                                        |           |                                         |
| -------------------------------------- | --------- | --------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the instance ID of the device to query. |

## Return Value

(const char *) Returns the name of the audio device, or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAudioPlaybackDevices](SDL_GetAudioPlaybackDevices)
- [SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

