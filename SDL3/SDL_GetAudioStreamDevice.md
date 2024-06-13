###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamDevice

Query an audio stream for its currently-bound device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioDeviceID SDL_GetAudioStreamDevice(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                            |
| ------------------------------------ | ---------- | -------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the audio stream to query. |

## Return Value

([SDL_AudioDeviceID](SDL_AudioDeviceID)) Returns the bound audio device, or
0 if not bound or invalid.

## Remarks

This reports the audio device that an audio stream is currently bound to.

If not bound, or invalid, this returns zero, which is not a valid device
ID.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BindAudioStream](SDL_BindAudioStream)
- [SDL_BindAudioStreams](SDL_BindAudioStreams)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

