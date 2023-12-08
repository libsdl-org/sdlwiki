###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockAudioDevice

Use this function to unlock the audio callback function for a specified device.

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
[SDL_LockAudioDevice](SDL_LockAudioDevice.md)() call.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LockAudioDevice](SDL_LockAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md)
