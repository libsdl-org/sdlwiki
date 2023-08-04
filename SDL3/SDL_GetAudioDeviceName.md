###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioDeviceName

Get the human-readable name of a specific audio device.

## Syntax

```c
char* SDL_GetAudioDeviceName(SDL_AudioDeviceID devid);

```

## Function Parameters

|               |                                         |
| ------------- | --------------------------------------- |
| **devid**     | the instance ID of the device to query. |

## Return Value

Returns the name of the audio device, or NULL on error.

## Remarks

The string returned by this function is UTF-8 encoded. The caller should
call [SDL_free](SDL_free) on the return value when done with it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
int i, count = SDL_GetNumAudioDevices(0);

for (i = 0; i < count; ++i) {
    SDL_Log("Audio device %d: %s", i, SDL_GetAudioDeviceName(i, 0));
}
```

## Related Functions

* [SDL_GetNumAudioDevices](SDL_GetNumAudioDevices)
* [SDL_GetDefaultAudioInfo](SDL_GetDefaultAudioInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAudio](CategoryAudio)


