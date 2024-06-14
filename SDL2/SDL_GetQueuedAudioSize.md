###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetQueuedAudioSize

Get the number of bytes of still-queued audio.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
Uint32 SDL_GetQueuedAudioSize(SDL_AudioDeviceID dev);
```

## Function Parameters

|                                        |         |                                                         |
| -------------------------------------- | ------- | ------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev** | the device ID of which we will query queued audio size. |

## Return Value

(Uint32) Returns the number of bytes (not samples!) of queued audio.

## Remarks

For playback devices: this is the number of bytes that have been queued for
playback with [SDL_QueueAudio](SDL_QueueAudio)(), but have not yet been
sent to the hardware.

Once we've sent it to the hardware, this function can not decide the exact
byte boundary of what has been played. It's possible that we just gave the
hardware several kilobytes right before you called this function, but it
hasn't played any of it yet, or maybe half of it, etc.

For capture devices, this is the number of bytes that have been captured by
the device and are waiting for you to dequeue. This number may grow at any
time, so this only informs of the lower-bound of available data.

You may not queue or dequeue audio on a device that is using an
application-supplied callback; calling this function on such a device
always returns 0. You have to use the audio callback or queue audio, but
not both.

You should not call [SDL_LockAudio](SDL_LockAudio)() on the device before
querying; SDL handles locking internally for this function.

## Version

This function is available since SDL 2.0.4.

## See Also

- [SDL_ClearQueuedAudio](SDL_ClearQueuedAudio)
- [SDL_QueueAudio](SDL_QueueAudio)
- [SDL_DequeueAudio](SDL_DequeueAudio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

