###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioPlaybackDevices

Get a list of currently-connected audio playback devices.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
const SDL_AudioDeviceID * SDL_GetAudioPlaybackDevices(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of devices returned, may be NULL. |

## Return Value

(const [SDL_AudioDeviceID](SDL_AudioDeviceID) *) Returns a 0 terminated
array of device instance IDs or NULL on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns of list of available devices that play sound, perhaps to
speakers or headphones ("playback" devices). If you want devices that
record audio, like a microphone ("recording" devices), use
[SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)() instead.

This only returns a list of physical devices; it will not have any device
IDs returned by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)().

If this function returns NULL, to signify an error, `*count` will be set to
zero.

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenAudioDevice](SDL_OpenAudioDevice)
- [SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

