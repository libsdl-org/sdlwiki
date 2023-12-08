###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockAudioDevice

Use this function to lock out the audio callback function for a specified device.

## Syntax

```c
void SDL_LockAudioDevice(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                   |
| ----------- | --------------------------------- |
| **dev**     | the ID of the device to be locked |

## Remarks

The lock manipulated by these functions protects the audio callback
function specified in [SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)(). During
a
[SDL_LockAudioDevice](SDL_LockAudioDevice.md)()/[SDL_UnlockAudioDevice](SDL_UnlockAudioDevice.md)()
pair, you can be guaranteed that the callback function for that device is
not running, even if the device is not paused. While a device is locked,
any other unpaused, unlocked devices may still run their callbacks.

Calling this function from inside your audio callback is unnecessary. SDL
obtains this lock before calling your function, and releases it when the
function returns.

You should not hold the lock longer than absolutely necessary. If you hold
it too long, you'll experience dropouts in your audio playback. Ideally,
your application locks the device, sets a few variables and unlocks again.
Do not do heavy work while holding the lock for a device.

It is safe to lock the audio device multiple times, as long as you unlock
it an equivalent number of times. The callback will not run until the
device has been unlocked completely in this way. If your application fails
to unlock the device appropriately, your callback will never run, you might
hear repeating bursts of audio, and
[SDL_CloseAudioDevice](SDL_CloseAudioDevice.md)() will probably deadlock.

Internally, the audio device lock is a mutex; if you lock from two threads
at once, not only will you block the audio callback, you'll block the other
thread.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_UnlockAudioDevice](SDL_UnlockAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md)
