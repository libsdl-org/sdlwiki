###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAudioRecordingDevices

Get a list of currently-connected audio recording devices.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioDeviceID * SDL_GetAudioRecordingDevices(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of devices returned, may be NULL. |

## Return Value

([SDL_AudioDeviceID](SDL_AudioDeviceID) *) Returns a 0 terminated array of
device instance IDs, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

This returns of list of available devices that record audio, like a
microphone ("recording" devices). If you want devices that play sound,
perhaps to speakers or headphones ("playback" devices), use
[SDL_GetAudioPlaybackDevices](SDL_GetAudioPlaybackDevices)() instead.

This only returns a list of physical devices; it will not have any device
IDs returned by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)().

If this function returns NULL, to signify an error, `*count` will be set to
zero.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_OpenAudioDevice](SDL_OpenAudioDevice)
- [SDL_GetAudioPlaybackDevices](SDL_GetAudioPlaybackDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

