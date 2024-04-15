###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PauseAudioDevice

Use this function to pause audio playback on a specified device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_PauseAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                                 |
| ----------- | --------------------------------------------------------------- |
| **dev**     | a device opened by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function pauses audio processing for a given device. Any bound audio
streams will not progress, and no audio will be generated. Pausing one
device does not prevent other unpaused devices from running.

Unlike in SDL2, audio devices start in an _unpaused_ state, since an app
has to bind a stream before any audio will flow. Pausing a paused device is
a legal no-op.

Pausing a device can be useful to halt all audio without unbinding all the
audio streams. This might be useful while a game is paused, or a level is
loading, etc.

Physical devices can not be paused or unpaused, only logical devices
created through [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() can be.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_AudioDeviceID devid;
SDL_PauseAudioDevice(devid);  // audio callback is stopped when this returns.
SDL_Delay(5000);  // audio device plays silence for 5 seconds
SDL_PlayAudioDevice(devid);  // audio callback starts running again.
```

## See Also

* [SDL_ResumeAudioDevice](SDL_ResumeAudioDevice)
* [SDL_AudioDevicePaused](SDL_AudioDevicePaused)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)


