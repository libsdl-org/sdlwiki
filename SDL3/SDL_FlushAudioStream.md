###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlushAudioStream

Tell the stream that you're done sending data, and anything being buffered should be converted/resampled and made available immediately.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
int SDL_FlushAudioStream(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                           |
| ------------------------------------ | ---------- | ------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | The audio stream to flush |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

It is legal to add more data to a stream after flushing, but there may be
audio gaps in the output. Generally this is intended to signal the end of
input, so the complete output becomes available.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PutAudioStreamData](SDL_PutAudioStreamData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

