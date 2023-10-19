###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateAudioStream

Create a new audio stream.

## Syntax

```c
SDL_AudioStream* SDL_CreateAudioStream(const SDL_AudioSpec *src_spec, const SDL_AudioSpec *dst_spec);

```

## Function Parameters

|                  |                                        |
| ---------------- | -------------------------------------- |
| **src_spec**     | The format details of the input audio  |
| **dst_spec**     | The format details of the output audio |

## Return Value

Returns a new audio stream on success, or NULL on failure.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_ChangeAudioStreamOutput](SDL_ChangeAudioStreamOutput)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

