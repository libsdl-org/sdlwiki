###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamData

Get converted/resampled data from the stream 

## Syntax

```c
int SDL_GetAudioStreamData(SDL_AudioStream *stream, void *buf, int len);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **stream**     | The stream the audio is being requested from |
| **buf**        | A buffer to fill with audio data             |
| **len**        | The maximum number of bytes to fill          |

## Return Value

Returns the number of bytes read from the stream, or -1 on error

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

