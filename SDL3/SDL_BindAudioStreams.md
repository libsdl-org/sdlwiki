###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindAudioStreams

Bind a list of audio streams to an audio device.

## Syntax

```c
int SDL_BindAudioStreams(SDL_AudioDeviceID devid, SDL_AudioStream **streams, int num_streams);

```

## Function Parameters

|                     |                                               |
| ------------------- | --------------------------------------------- |
| **devid**           | an audio device to bind a stream to.          |
| **streams**         | an array of audio streams to unbind.          |
| **num_streams**     | Number streams listed in the `streams` array. |

## Return Value

Returns 0 on success, -1 on error; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Audio data will flow through any bound streams. For an output device, data
for all bound streams will be mixed together and fed to the device. For a
capture device, a copy of recorded data will be provided to each bound
stream.

Audio streams can only be bound to an open device. This operation is
atomic--all streams bound in the same call will start processing at the
same time, so they can stay in sync. Also: either all streams will be bound
or none of them will be.

It is an error to bind an already-bound stream; it must be explicitly
unbound first.

Binding a stream to a device will set its output format for output devices,
and its input format for capture devices, so they match the device's
settings. The caller is welcome to change the other end of the stream's
format at any time.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BindAudioStreams](SDL_BindAudioStreams)
* [SDL_UnbindAudioStreams](SDL_UnbindAudioStreams)
* [SDL_UnbindAudioStream](SDL_UnbindAudioStream)
* [SDL_GetAudioStreamDevice](SDL_GetAudioStreamDevice)

----
[CategoryAPI](CategoryAPI)

