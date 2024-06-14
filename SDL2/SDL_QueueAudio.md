###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QueueAudio

Queue more audio on non-callback devices.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
int SDL_QueueAudio(SDL_AudioDeviceID dev, const void *data, Uint32 len);
```

## Function Parameters

|                                        |          |                                                            |
| -------------------------------------- | -------- | ---------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev**  | the device ID to which we will queue audio.                |
| const void *                           | **data** | the data to queue to the device for later playback.        |
| Uint32                                 | **len**  | the number of bytes (not samples!) to which `data` points. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If you are looking to retrieve queued audio from a non-callback capture
device, you want [SDL_DequeueAudio](SDL_DequeueAudio)() instead.
[SDL_QueueAudio](SDL_QueueAudio)() will return -1 to signify an error if
you use it with capture devices.

SDL offers two ways to feed audio to the device: you can either supply a
callback that SDL triggers with some frequency to obtain more audio (pull
method), or you can supply no callback, and then SDL will expect you to
supply data at regular intervals (push method) with this function.

There are no limits on the amount of data you can queue, short of
exhaustion of address space. Queued data will drain to the device as
necessary without further intervention from you. If the device needs audio
but there is not enough queued, it will play silence to make up the
difference. This means you will have skips in your audio playback if you
aren't routinely queueing sufficient data.

This function copies the supplied data, so you are safe to free it when the
function returns. This function is thread-safe, but queueing to the same
device from two threads at once does not promise which buffer will be
queued first.

You may not queue audio on a device that is using an application-supplied
callback; doing so returns an error. You have to use the audio callback or
queue audio with this function, but not both.

You should not call [SDL_LockAudio](SDL_LockAudio)() on the device before
queueing; SDL handles locking internally for this function.

Note that SDL2 does not support planar audio. You will need to resample
from planar audio formats into a non-planar one (see
[SDL_AudioFormat](SDL_AudioFormat)) before queuing audio.

## Version

This function is available since SDL 2.0.4.

## See Also

- [SDL_ClearQueuedAudio](SDL_ClearQueuedAudio)
- [SDL_GetQueuedAudioSize](SDL_GetQueuedAudioSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

