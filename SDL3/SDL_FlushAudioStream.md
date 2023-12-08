###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlushAudioStream

Tell the stream that you're done sending data, and anything being buffered should be converted/resampled and made available immediately.

## Syntax

```c
int SDL_FlushAudioStream(SDL_AudioStream *stream);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **stream**     | The audio stream to flush |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

It is legal to add more data to a stream after flushing, but there will be
audio gaps in the output. Generally this is intended to signal the end of
input, so the complete output becomes available.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream.md)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData.md)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData.md)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable.md)
* [SDL_ClearAudioStream](SDL_ClearAudioStream.md)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
