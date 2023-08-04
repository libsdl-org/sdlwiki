###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateAndBindAudioStream

Convenience function to create and bind an audio stream in one step.

## Syntax

```c
SDL_AudioStream* SDL_CreateAndBindAudioStream(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);

```

## Function Parameters

|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| **devid**     | an audio device to bind a stream to. This must be an opened device, and can not be zero. |
| **spec**      | the audio stream's input format                                                          |

## Return Value

Returns a bound audio stream on success, ready to use. NULL on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This manages the creation of an audio stream, and setting its format
correctly to match both the app and the audio device's needs. This is
optional, but slightly less cumbersome to set up for a common use case.

The `spec` parameter represents the app's side of the audio stream. That
is, for recording audio, this will be the output format, and for playing
audio, this will be the input format. This function will set the other side
of the audio stream to the device's format.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BindAudioStreams](SDL_BindAudioStreams)
* [SDL_UnbindAudioStreams](SDL_UnbindAudioStreams)
* [SDL_UnbindAudioStream](SDL_UnbindAudioStream)

----
[CategoryAPI](CategoryAPI)

