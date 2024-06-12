###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CloseAudioDevice

Use this function to shut down audio processing and close the audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_CloseAudioDevice(SDL_AudioDeviceID dev);
```

## Function Parameters

|                                        |         |                                                                                     |
| -------------------------------------- | ------- | ----------------------------------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev** | an audio device previously opened with [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() |

## Remarks

The application should close open audio devices once they are no longer
needed. Calling this function will wait until the device's audio callback
is not running, release the audio hardware and then clean up internal
state. No further audio will play from this device once this function
returns.

This function may block briefly while pending audio data is played by the
hardware, so that applications don't drop the last buffer of data they
supplied.

The device ID is invalid as soon as the device is closed, and is eligible
for reuse in a new [SDL_OpenAudioDevice](SDL_OpenAudioDevice)() call
immediately.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_OpenAudioDevice](SDL_OpenAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

