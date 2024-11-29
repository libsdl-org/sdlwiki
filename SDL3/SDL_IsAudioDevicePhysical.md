###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IsAudioDevicePhysical

Determine if an audio device is physical (instead of logical).

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_IsAudioDevicePhysical(SDL_AudioDeviceID devid);
```

## Function Parameters

|                                        |           |                         |
| -------------------------------------- | --------- | ----------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the device ID to query. |

## Return Value

(bool) Returns true if devid is a physical device, false if it is logical.

## Remarks

An [SDL_AudioDeviceID](SDL_AudioDeviceID) that represents physical hardare
is a physical device; there is one for each piece of hardware that SDL can
see. Logical devices are created by calling
[SDL_OpenAudioDevice](SDL_OpenAudioDevice) or
[SDL_OpenAudioDeviceStream](SDL_OpenAudioDeviceStream), and while each is
associated with a physical device, there can be any number of logical
devices on one physical device.

For the most part, logical and physical IDs are interchangeable--if you try
to open a logical device, SDL understands to assign that effort to the
underlying physical device, etc. However, it might be useful to know if an
arbitrary device ID is physical or logical. This function reports which.

This function may return either true or false for invalid device IDs.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

