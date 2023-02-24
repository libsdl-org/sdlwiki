###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateAudioStream

Create a new audio stream.

## Syntax

```c
SDL_AudioStream* SDL_CreateAudioStream(SDL_AudioFormat src_format,
                                    Uint8 src_channels,
                                    int src_rate,
                                    SDL_AudioFormat dst_format,
                                    Uint8 dst_channels,
                                    int dst_rate);

```

## Function Parameters

|                      |                                                    |
| -------------------- | -------------------------------------------------- |
| **src_format**       | The format of the source audio                     |
| **src_channels**     | The number of channels of the source audio         |
| **src_rate**         | The sampling rate of the source audio              |
| **dst_format**       | The format of the desired audio output             |
| **dst_channels**     | The number of channels of the desired audio output |
| **dst_rate**         | The sampling rate of the desired audio output      |

## Return Value

Returns 0 on success, or -1 on error.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
* [SDL_FlushAudioStream](SDL_FlushAudioStream)
* [SDL_ClearAudioStream](SDL_ClearAudioStream)
* [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI)

