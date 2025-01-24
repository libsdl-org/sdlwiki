# SDL_GetAudioPlaybackDevices

Get a list of currently-connected audio playback devices.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioDeviceID * SDL_GetAudioPlaybackDevices(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of devices returned, may be NULL. |

## Return Value

([SDL_AudioDeviceID](SDL_AudioDeviceID) *) Returns a 0 terminated array of
device instance IDs or NULL on error; call [SDL_GetError](SDL_GetError)()
for more information. This should be freed with [SDL_free](SDL_free)() when
it is no longer needed.

## Remarks

This returns of list of available devices that play sound, perhaps to
speakers or headphones ("playback" devices). If you want devices that
record audio, like a microphone ("recording" devices), use
[SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)() instead.

This only returns a list of physical devices; it will not have any device
IDs returned by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)().

If this function returns NULL, to signify an error, `*count` will be set to
zero.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_OpenAudioDevice](SDL_OpenAudioDevice)
- [SDL_GetAudioRecordingDevices](SDL_GetAudioRecordingDevices)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

