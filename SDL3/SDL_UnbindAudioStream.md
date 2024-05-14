###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnbindAudioStream

Unbind a single audio stream from its audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
void SDL_UnbindAudioStream(SDL_AudioStream *stream);

```

## Function Parameters

|                |                                          |
| -------------- | ---------------------------------------- |
| **stream**     | an audio stream to unbind from a device. |

## Remarks

This is a convenience function, equivalent to calling
`SDL_UnbindAudioStreams(&stream, 1)`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BindAudioStream](SDL_BindAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

