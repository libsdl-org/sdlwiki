# SDL_BindAudioStreams

Bind a list of audio streams to an audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_BindAudioStreams(SDL_AudioDeviceID devid, SDL_AudioStream * const *streams, int num_streams);
```

## Function Parameters

|                                              |                 |                                               |
| -------------------------------------------- | --------------- | --------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID)       | **devid**       | an audio device to bind a stream to.          |
| [SDL_AudioStream](SDL_AudioStream) * const * | **streams**     | an array of audio streams to bind.            |
| int                                          | **num_streams** | number streams listed in the `streams` array. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Audio data will flow through any bound streams. For a playback device, data
for all bound streams will be mixed together and fed to the device. For a
recording device, a copy of recorded data will be provided to each bound
stream.

Audio streams can only be bound to an open device. This operation is
atomic--all streams bound in the same call will start processing at the
same time, so they can stay in sync. Also: either all streams will be bound
or none of them will be.

It is an error to bind an already-bound stream; it must be explicitly
unbound first.

Binding a stream to a device will set its output format for playback
devices, and its input format for recording devices, so they match the
device's settings. The caller is welcome to change the other end of the
stream's format at any time with
[SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat)(). If the other end of
the stream's format has never been set (the audio stream was created with a
NULL audio spec), this function will set it to match the device end's
format.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_BindAudioStreams](SDL_BindAudioStreams)
- [SDL_UnbindAudioStream](SDL_UnbindAudioStream)
- [SDL_GetAudioStreamDevice](SDL_GetAudioStreamDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

