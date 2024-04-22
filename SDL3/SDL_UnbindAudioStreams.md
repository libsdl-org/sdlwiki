###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnbindAudioStreams

Unbind a list of audio streams from their audio devices.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
void SDL_UnbindAudioStreams(SDL_AudioStream **streams, int num_streams);

```

## Function Parameters

|                     |                                               |
| ------------------- | --------------------------------------------- |
| **streams**         | an array of audio streams to unbind.          |
| **num_streams**     | Number streams listed in the `streams` array. |

## Remarks

The streams being unbound do not all have to be on the same device. All
streams on the same device will be unbound atomically (data will stop
flowing through them all unbound streams on the same device at the same
time).

Unbinding a stream that isn't bound to a device is a legal no-op.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_BindAudioStreams](SDL_BindAudioStreams)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

