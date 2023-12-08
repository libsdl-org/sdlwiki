###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioDeviceStatus

Use this function to get the current audio state of an audio device.

## Syntax

```c
SDL_AudioStatus SDL_GetAudioDeviceStatus(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------- |
| **dev**     | the ID of an audio device previously opened with [SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)() |

## Return Value

Returns the [SDL_AudioStatus](SDL_AudioStatus.md) of the specified audio
device.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_AudioStatus](SDL_AudioStatus.md), , , from="== Code Examples ==", to="== Remarks ==")>>

## Related Functions

* [SDL_PlayAudioDevice](SDL_PlayAudioDevice.md)
* [SDL_PauseAudioDevice](SDL_PauseAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
