###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioOutputDevices

Get a list of currently-connected audio output devices.

## Syntax

```c
SDL_AudioDeviceID* SDL_GetAudioOutputDevices(int *count);

```

## Function Parameters

|               |                                                         |
| ------------- | ------------------------------------------------------- |
| **count**     | a pointer filled in with the number of devices returned |

## Return Value

Returns a 0 terminated array of device instance IDs which should be freed
with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

This returns of list of available devices that play sound, perhaps to
speakers or headphones ("output" devices). If you want devices that record
audio, like a microphone ("capture" devices), use
[SDL_GetAudioCaptureDevices](SDL_GetAudioCaptureDevices)() instead.

This only returns a list of physical devices; it will not have any device
IDs returned by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenAudioDevice](SDL_OpenAudioDevice)
* [SDL_GetAudioCaptureDevices](SDL_GetAudioCaptureDevices)

----
[CategoryAPI](CategoryAPI)

