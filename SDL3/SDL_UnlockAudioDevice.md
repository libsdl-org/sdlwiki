###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Code Examples

```c++
void MyAudioCallback(void *userdata, Uint8* stream, int len)
{
    printf("The audio callback is running!\n");
    SDL_memset(stream, 0, len);  // just silence.
    printf("The audio callback is done!\n");
}

// don't lock for 2 seconds at a time in real life, please.
extern SDL_AudioDeviceID devid;
SDL_Delay(2000);  // callback runs for 2 seconds.
SDL_LockAudioDevice(devid);
printf("The audio callback can't be running right now!\n");
SDL_Delay(2000);  // callback doesn't run for 2 seconds.
printf("Ok, unlocking!\n");
SDL_UnlockAudioDevice(devid);
SDL_Delay(2000);  // callback runs for 2 seconds.
```

## Related Functions

* [SDL_LockAudioDevice](SDL_LockAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
