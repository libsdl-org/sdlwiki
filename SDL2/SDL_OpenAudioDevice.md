###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_OpenAudioDevice

Open a specific audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
SDL_AudioDeviceID SDL_OpenAudioDevice(
                      const char *device,
                      int iscapture,
                      const SDL_AudioSpec *desired,
                      SDL_AudioSpec *obtained,
                      int allowed_changes);
```

## Function Parameters

|                                        |                     |                                                                                                                                                                           |
| -------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char *                           | **device**          | a UTF-8 string reported by [SDL_GetAudioDeviceName](SDL_GetAudioDeviceName)() or a driver-specific name as appropriate. NULL requests the most reasonable default device. |
| int                                    | **iscapture**       | non-zero to specify a device should be opened for recording, not playback.                                                                                                |
| const [SDL_AudioSpec](SDL_AudioSpec) * | **desired**         | an [SDL_AudioSpec](SDL_AudioSpec) structure representing the desired output format; see [SDL_OpenAudio](SDL_OpenAudio)() for more information.                            |
| [SDL_AudioSpec](SDL_AudioSpec) *       | **obtained**        | an [SDL_AudioSpec](SDL_AudioSpec) structure filled in with the actual output format; see [SDL_OpenAudio](SDL_OpenAudio)() for more information.                           |
| int                                    | **allowed_changes** | 0, or one or more flags OR'd together.                                                                                                                                    |

## Return Value

([SDL_AudioDeviceID](SDL_AudioDeviceID)) Returns a valid device ID that is
> 0 on success or 0 on failure; call [SDL_GetError](SDL_GetError)() for
more information.

For compatibility with SDL 1.2, this will never return 1, since SDL
reserves that ID for the legacy [SDL_OpenAudio](SDL_OpenAudio)() function.

## Remarks

[SDL_OpenAudio](SDL_OpenAudio)(), unlike this function, always acts on
device ID 1. As such, this function will never return a 1 so as not to
conflict with the legacy function.

Please note that SDL 2.0 before 2.0.5 did not support recording; as such,
this function would fail if `iscapture` was not zero. Starting with SDL
2.0.5, recording is implemented and this value can be non-zero.

Passing in a `device` name of NULL requests the most reasonable default
(and is equivalent to what [SDL_OpenAudio](SDL_OpenAudio)() does to choose
a device). The `device` name is a UTF-8 string reported by
[SDL_GetAudioDeviceName](SDL_GetAudioDeviceName)(), but some drivers allow
arbitrary and driver-specific strings, such as a hostname/IP address for a
remote audio server, or a filename in the diskaudio driver.

An opened audio device starts out paused, and should be enabled for playing
by calling [SDL_PauseAudioDevice](SDL_PauseAudioDevice)(devid, 0) when you
are ready for your audio callback function to be called. Since the audio
driver may modify the requested size of the audio buffer, you should
allocate any local mixing buffers after you open the audio device.

The audio callback runs in a separate thread in most cases; you can prevent
race conditions between your callback and other threads without fully
pausing playback with [SDL_LockAudioDevice](SDL_LockAudioDevice)(). For
more information about the callback, see [SDL_AudioSpec](SDL_AudioSpec).

Managing the audio spec via 'desired' and 'obtained':

When filling in the desired audio spec structure:

- `desired->freq` should be the frequency in sample-frames-per-second (Hz).
- `desired->format` should be the audio format
  ([`AUDIO_S16SYS`](AUDIO_S16SYS), etc).
- `desired->samples` is the desired size of the audio buffer, in _sample
  frames_ (with stereo output, two samples--left and right--would make a
  single sample frame). This number should be a power of two, and may be
  adjusted by the audio driver to a value more suitable for the hardware.
  Good values seem to range between 512 and 8096 inclusive, depending on
  the application and CPU speed. Smaller values reduce latency, but can
  lead to underflow if the application is doing heavy processing and cannot
  fill the audio buffer in time. Note that the number of sample frames is
  directly related to time by the following formula: `ms =
  (sampleframes*1000)/freq`
- `desired->size` is the size in _bytes_ of the audio buffer, and is
  calculated by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)(). You don't
  initialize this.
- `desired->silence` is the value used to set the buffer to silence, and is
  calculated by [SDL_OpenAudioDevice](SDL_OpenAudioDevice)(). You don't
  initialize this.
- `desired->callback` should be set to a function that will be called when
  the audio device is ready for more data. It is passed a pointer to the
  audio buffer, and the length in bytes of the audio buffer. This function
  usually runs in a separate thread, and so you should protect data
  structures that it accesses by calling
  [SDL_LockAudioDevice](SDL_LockAudioDevice)() and
  [SDL_UnlockAudioDevice](SDL_UnlockAudioDevice)() in your code.
  Alternately, you may pass a NULL pointer here, and call
  [SDL_QueueAudio](SDL_QueueAudio)() with some frequency, to queue more
  audio samples to be played (or for capture devices, call
  [SDL_DequeueAudio](SDL_DequeueAudio)() with some frequency, to obtain
  audio samples).
- `desired->userdata` is passed as the first parameter to your callback
  function. If you passed a NULL callback, this value is ignored.

`allowed_changes` can have the following flags OR'd together:

- [`SDL_AUDIO_ALLOW_FREQUENCY_CHANGE`](SDL_AUDIO_ALLOW_FREQUENCY_CHANGE)
- [`SDL_AUDIO_ALLOW_FORMAT_CHANGE`](SDL_AUDIO_ALLOW_FORMAT_CHANGE)
- [`SDL_AUDIO_ALLOW_CHANNELS_CHANGE`](SDL_AUDIO_ALLOW_CHANNELS_CHANGE)
- [`SDL_AUDIO_ALLOW_SAMPLES_CHANGE`](SDL_AUDIO_ALLOW_SAMPLES_CHANGE)
- [`SDL_AUDIO_ALLOW_ANY_CHANGE`](SDL_AUDIO_ALLOW_ANY_CHANGE)

These flags specify how SDL should behave when a device cannot offer a
specific feature. If the application requests a feature that the hardware
doesn't offer, SDL will always try to get the closest equivalent.

For example, if you ask for float32 audio format, but the sound card only
supports int16, SDL will set the hardware to int16. If you had set
[SDL_AUDIO_ALLOW_FORMAT_CHANGE](SDL_AUDIO_ALLOW_FORMAT_CHANGE), SDL will
change the format in the `obtained` structure. If that flag was *not* set,
SDL will prepare to convert your callback's float32 audio to int16 before
feeding it to the hardware and will keep the originally requested format in
the `obtained` structure.

The resulting audio specs, varying depending on hardware and on what
changes were allowed, will then be written back to `obtained`.

If your application can only handle one specific data format, pass a zero
for `allowed_changes` and let SDL transparently handle any differences.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CloseAudioDevice](SDL_CloseAudioDevice)
- [SDL_GetAudioDeviceName](SDL_GetAudioDeviceName)
- [SDL_LockAudioDevice](SDL_LockAudioDevice)
- [SDL_OpenAudio](SDL_OpenAudio)
- [SDL_PauseAudioDevice](SDL_PauseAudioDevice)
- [SDL_UnlockAudioDevice](SDL_UnlockAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

