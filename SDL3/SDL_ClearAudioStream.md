###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearAudioStream

Clear any pending data in the stream without converting it 

## Syntax

```c
int SDL_ClearAudioStream(SDL_AudioStream *stream);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **stream**     | The audio stream to clear |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

