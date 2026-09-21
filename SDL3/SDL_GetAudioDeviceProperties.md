# SDL_GetAudioDeviceProperties

Get the properties associated with an audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_PropertiesID SDL_GetAudioDeviceProperties(SDL_AudioDeviceID devid);
```

## Function Parameters

|                                        |           |                                        |
| -------------------------------------- | --------- | -------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the audio device instance id to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This can be used with both logical and physical devices. Note that while
apps can hang any data they want here, physical device IDs are global; it
would be better to assign data to one's own logical device so it doesn't
interfere with other parts of the program that might be using the same
physical device ID.

Properties provided by SDL for physical devices will also be made available
on their associated logical devices, unless otherwise noted.

The application can hang any data it wants here, but the following
properties are understood by SDL:

- [`SDL_PROP_AUDIO_DEVICE_UNIQUE_ID_STRING`](SDL_PROP_AUDIO_DEVICE_UNIQUE_ID_STRING):
  This identifier can be used to locate a specific device. In optimal
  conditions, this identifier will not change between runs of an app,
  hardware disconnection, and system reboots. However, depending on the
  hardware, operating system, and other circumstances, a device's
  identifier may change, so if the app cannot find a device with a
  previously queried identifier, the user should be prompted to choose a
  new device (possibly the same device, now with a new identifier). Device
  identifier strings have no specific format, the format may change in the
  future without warning, and are likely different between different
  operating systems on the same hardware. If the system cannot reasonably
  provide a unique identifier, this property will not be set. Note that
  property is useful for finding specific hardware again on a later run of
  the app, but often times it's better to just open the default device
  ([SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK](SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK)
  or
  [SDL_AUDIO_DEVICE_DEFAULT_RECORDING](SDL_AUDIO_DEVICE_DEFAULT_RECORDING)),
  and let the user set this up globally on their platform.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

