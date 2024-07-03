###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioDeviceGain

Get the gain of an audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
float SDL_GetAudioDeviceGain(SDL_AudioDeviceID devid);
```

## Function Parameters

|                                        |           |                            |
| -------------------------------------- | --------- | -------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the audio device to query. |

## Return Value

(float) Returns the gain of the device, or -1.0f on error.

## Remarks

The gain of a device is its volume; a larger gain means a louder output,
with a gain of zero being silence.

Audio devices default to a gain of 1.0f (no change in output).

Physical devices may not have their gain changed, only logical devices, and
this function will always return -1.0f when used on physical devices.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetAudioDeviceGain](SDL_SetAudioDeviceGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

