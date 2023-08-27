###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamDevice

Query an audio stream for its currently-bound device.

## Syntax

```c
SDL_AudioDeviceID SDL_GetAudioStreamDevice(SDL_AudioStream *stream);

```

## Function Parameters

|                |                            |
| -------------- | -------------------------- |
| **stream**     | the audio stream to query. |

## Return Value

Returns The bound audio device, or 0 if not bound or invalid.

## Remarks

This reports the audio device that an audio stream is currently bound to.

If not bound, or invalid, this returns zero, which is not a valid device
ID.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BindAudioStream](SDL_BindAudioStream)
* [SDL_BindAudioStreams](SDL_BindAudioStreams)
* [SDL_UnbindAudioStream](SDL_UnbindAudioStream)
* [SDL_UnbindAudioStreams](SDL_UnbindAudioStreams)

----
[CategoryAPI](CategoryAPI)

