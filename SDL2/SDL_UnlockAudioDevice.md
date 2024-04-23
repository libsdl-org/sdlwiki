###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockAudioDevice

Use this function to unlock the audio callback function for a specified device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_UnlockAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                     |
| ----------- | ----------------------------------- |
| **dev**     | the ID of the device to be unlocked |

## Remarks

This function should be paired with a previous
[SDL_LockAudioDevice](SDL_LockAudioDevice)() call.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LockAudioDevice](SDL_LockAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


