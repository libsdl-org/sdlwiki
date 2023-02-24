###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PutAudioStreamData

Add data to be converted/resampled to the stream.

## Syntax

```c
int SDL_PutAudioStreamData(SDL_AudioStream *stream, const void *buf, int len);

```

## Function Parameters

|                |                                             |
| -------------- | ------------------------------------------- |
| **stream**     | The stream the audio data is being added to |
| **buf**        | A pointer to the audio data to add          |
| **len**        | The number of bytes to write to the stream  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

