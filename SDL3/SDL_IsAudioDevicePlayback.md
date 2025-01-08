###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IsAudioDevicePlayback

Determine if an audio device is a playback device (instead of recording).

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_IsAudioDevicePlayback(SDL_AudioDeviceID devid);
```

## Function Parameters

|                                        |           |                         |
| -------------------------------------- | --------- | ----------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the device ID to query. |

## Return Value

(bool) Returns true if devid is a playback device, false if it is
recording.

## Remarks

This function may return either true or false for invalid device IDs.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.8.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

