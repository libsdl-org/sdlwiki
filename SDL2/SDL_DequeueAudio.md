# SDL_DequeueAudio

Dequeue more audio on non-callback devices.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
Uint32 SDL_DequeueAudio(SDL_AudioDeviceID dev, void *data, Uint32 len);
```

## Function Parameters

|                                        |          |                                                            |
| -------------------------------------- | -------- | ---------------------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **dev**  | the device ID from which we will dequeue audio.            |
| void *                                 | **data** | a pointer into where audio data should be copied.          |
| [Uint32](Uint32)                       | **len**  | the number of bytes (not samples!) to which (data) points. |

## Return Value

([Uint32](Uint32)) Returns the number of bytes dequeued, which could be
less than requested; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

If you are looking to queue audio for output on a non-callback playback
device, you want [SDL_QueueAudio](SDL_QueueAudio)() instead.
[SDL_DequeueAudio](SDL_DequeueAudio)() will always return 0 if you use it
with playback devices.

SDL offers two ways to retrieve audio from a capture device: you can either
supply a callback that SDL triggers with some frequency as the device
records more audio data, (push method), or you can supply no callback, and
then SDL will expect you to retrieve data at regular intervals (pull
method) with this function.

There are no limits on the amount of data you can queue, short of
exhaustion of address space. Data from the device will keep queuing as
necessary without further intervention from you. This means you will
eventually run out of memory if you aren't routinely dequeueing data.

Capture devices will not queue data when paused; if you are expecting to
not need captured audio for some length of time, use
[SDL_PauseAudioDevice](SDL_PauseAudioDevice)() to stop the capture device
from queueing more data. This can be useful during, say, level loading
times. When unpaused, capture devices will start queueing data from that
point, having flushed any capturable data available while paused.

This function is thread-safe, but dequeueing from the same device from two
threads at once does not promise which thread will dequeue data first.

You may not dequeue audio from a device that is using an
application-supplied callback; doing so returns an error. You have to use
the audio callback, or dequeue audio with this function, but not both.

You should not call [SDL_LockAudio](SDL_LockAudio)() on the device before
dequeueing; SDL handles locking internally for this function.

## Version

This function is available since SDL 2.0.5.

## See Also

- [SDL_ClearQueuedAudio](SDL_ClearQueuedAudio)
- [SDL_GetQueuedAudioSize](SDL_GetQueuedAudioSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

