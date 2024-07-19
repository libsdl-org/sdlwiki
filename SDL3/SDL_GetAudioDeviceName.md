###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
int count;
SDL_AudioDeviceID *devices;
devices = SDL_GetAudioOutputDevices(&count);

for (int i = 0; i < count; ++i) {
    SDL_Log("Audio device %d: %s", i, SDL_GetAudioDeviceName(devices[i]));
}

SDL_free(devices);
```

## See Also

- [SDL_GetAudioPlaybackDevices](SDL_GetAudioPlaybackDevices)
- [SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)
- [SDL_GetDefaultAudioInfo](SDL_GetDefaultAudioInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

