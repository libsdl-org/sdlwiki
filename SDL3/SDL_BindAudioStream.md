###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BindAudioStream

Bind a single audio stream to an audio device.

## Syntax

```c
int SDL_BindAudioStream(SDL_AudioDeviceID devid, SDL_AudioStream *stream);

```

## Function Parameters

|                |                                      |
| -------------- | ------------------------------------ |
| **devid**      | an audio device to bind a stream to. |
| **stream**     | an audio stream to bind to a device. |

## Return Value

Returns 0 on success, -1 on error; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This is a convenience function, equivalent to calling
`SDL_BindAudioStreams(devid, &stream, 1)`.

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

