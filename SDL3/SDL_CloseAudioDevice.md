###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseAudioDevice

Close a previously-opened audio device.

## Syntax

```c
void SDL_CloseAudioDevice(SDL_AudioDeviceID devid);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **devid**     | an audio device id previously returned by [SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)() |

## Remarks

The application should close open audio devices once they are no longer
needed.

This function may block briefly while pending audio data is played by the
hardware, so that applications don't drop the last buffer of data they
supplied if terminating immediately afterwards.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_AudioSpec want;
SDL_AudioDeviceID devid = SDL_OpenAudioDevice(NULL, 0, &want, NULL, 0);
if (devid > 0) {
    SDL_PauseAudioDevice(devid, 0);
    SDL_Delay(5000);  // let audio callback run for 5 seconds.
    SDL_CloseAudioDevice(devid);
}
```

## Related Functions

* [SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
