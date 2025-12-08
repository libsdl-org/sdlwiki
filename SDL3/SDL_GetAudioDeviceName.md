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

## Remarks

**WARNING**: this function will work with
[SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK](SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK) and
[SDL_AUDIO_DEVICE_DEFAULT_RECORDING](SDL_AUDIO_DEVICE_DEFAULT_RECORDING),
returning the current default physical devices' names. However, as the
default device may change at any time, it is likely better to show a
generic name to the user, like "System default audio device" or perhaps
"default [currently %s]". Do not store this name to disk to reidentify the
device in a later run of the program, as the default might change in
general, and the string will be the name of a specific device and not the
abstract system default.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAudioPlaybackDevices](SDL_GetAudioPlaybackDevices)
- [SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

