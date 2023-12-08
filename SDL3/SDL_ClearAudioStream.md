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
[SDL_GetError](SDL_GetError.md)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream.md)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData.md)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData.md)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable.md)
* [SDL_FlushAudioStream](SDL_FlushAudioStream.md)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
