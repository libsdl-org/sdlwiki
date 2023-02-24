###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamAvailable

Get the number of converted/resampled bytes available.

## Syntax

```c
int SDL_GetAudioStreamAvailable(SDL_AudioStream *stream);

```

## Function Parameters

|                |                           |
| -------------- | ------------------------- |
| **stream**     | The audio stream to query |

## Return Value

Returns the number of converted/resampled bytes available.

## Remarks

The stream may be buffering data behind the scenes until it has enough to
resample correctly, so this number might be lower than what you expect, or
even be zero. Add more data or flush the stream if you need the data now.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

