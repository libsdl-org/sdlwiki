###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearQueuedAudio

Drop any queued audio data waiting to be sent to the hardware.

## Syntax

```c
int SDL_ClearQueuedAudio(SDL_AudioDeviceID dev);

```

## Function Parameters

|             |                                                 |
| ----------- | ----------------------------------------------- |
| **dev**     | the device ID of which to clear the audio queue |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Immediately after this call,
[SDL_GetQueuedAudioSize](SDL_GetQueuedAudioSize.md)() will return 0. For
output devices, the hardware will start playing silence if more audio isn't
queued. For capture devices, the hardware will start filling the empty
queue with new data if the capture device isn't paused.

This will not prevent playback of queued audio that's already been sent to
the hardware, as we can not undo that, so expect there to be some fraction
of a second of audio that might still be heard. This can be useful if you
want to, say, drop any pending music or any unprocessed microphone input
during a level change in your game.

You may not queue or dequeue audio on a device that is using an
application-supplied callback; calling this function on such a device
always returns 0. You have to use the audio callback or queue audio, but
not both.

You should not call [SDL_LockAudio](SDL_LockAudio.md)() on the device before
clearing the queue; SDL handles locking internally for this function.

This function always succeeds and thus returns void.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetQueuedAudioSize](SDL_GetQueuedAudioSize.md)
* [SDL_QueueAudio](SDL_QueueAudio.md)
* [SDL_DequeueAudio](SDL_DequeueAudio.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
