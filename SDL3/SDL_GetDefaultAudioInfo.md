###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDefaultAudioInfo

Get the name and preferred format of the default audio device.

## Syntax

```c
int SDL_GetDefaultAudioInfo(char **name,
                            SDL_AudioSpec *spec,
                            int iscapture);

```

## Function Parameters

|                   |                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name**          | A pointer to be filled with the name of the default device (can be NULL). Please call [SDL_free](SDL_free)() when you are done with this pointer! |
| **spec**          | The [SDL_AudioSpec](SDL_AudioSpec) to be initialized by this function.                                                                            |
| **iscapture**     | non-zero to query the default recording device, zero to query the default output device.                                                          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Some (but not all!) platforms have an isolated mechanism to get information
about the "default" device. This can actually be a completely different
device that's not in the list you get from
[SDL_GetAudioDeviceSpec](SDL_GetAudioDeviceSpec)(). It can even be a
network address! (This is discussed in
[SDL_OpenAudioDevice](SDL_OpenAudioDevice)().)

As a result, this call is not guaranteed to be performant, as it can query
the sound server directly every time, unlike the other query functions. You
should call this function sparingly!

`spec` will be filled with the sample rate, sample format, and channel
count, if a default device exists on the system. If `name` is provided,
will be filled with either a dynamically-allocated UTF-8 string or NULL.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAudioDeviceName](SDL_GetAudioDeviceName)
* [SDL_GetAudioDeviceSpec](SDL_GetAudioDeviceSpec)
* [SDL_OpenAudioDevice](SDL_OpenAudioDevice)

----
[CategoryAPI](CategoryAPI)

