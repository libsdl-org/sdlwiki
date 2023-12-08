###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_NewAudioStream

Create a new audio stream.

## Syntax

```c
SDL_AudioStream * SDL_NewAudioStream(const SDL_AudioFormat src_format,
                   const Uint8 src_channels,
                   const int src_rate,
                   const SDL_AudioFormat dst_format,
                   const Uint8 dst_channels,
                   const int dst_rate);

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

This function is available since SDL 2.0.7.

## Related Functions

* [SDL_AudioStreamPut](SDL_AudioStreamPut.md)
* [SDL_AudioStreamGet](SDL_AudioStreamGet.md)
* [SDL_AudioStreamAvailable](SDL_AudioStreamAvailable.md)
* [SDL_AudioStreamFlush](SDL_AudioStreamFlush.md)
* [SDL_AudioStreamClear](SDL_AudioStreamClear.md)
* [SDL_FreeAudioStream](SDL_FreeAudioStream.md)

----
[CategoryAPI](CategoryAPI.md)
