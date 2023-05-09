###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertAudioSamples

Convert some audio data of one format to another format.

## Syntax

```c
int SDL_ConvertAudioSamples(SDL_AudioFormat src_format,
                            Uint8 src_channels,
                            int src_rate,
                            const Uint8 *src_data,
                            int src_len,
                            SDL_AudioFormat dst_format,
                            Uint8 dst_channels,
                            int dst_rate,
                            Uint8 **dst_data,
                            int *dst_len);

```

## Function Parameters

|                      |                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **src_format**       | The format of the source audio                                                                                                       |
| **src_channels**     | The number of channels of the source audio                                                                                           |
| **src_rate**         | The sampling rate of the source audio                                                                                                |
| **src_data**         | The audio data to be converted                                                                                                       |
| **src_len**          | The len of src_data                                                                                                                  |
| **dst_format**       | The format of the desired audio output                                                                                               |
| **dst_channels**     | The number of channels of the desired audio output                                                                                   |
| **dst_rate**         | The sampling rate of the desired audio output                                                                                        |
| **dst_data**         | Will be filled with a pointer to converted audio data, which should be freed with [SDL_free](SDL_free)(). On error, it will be NULL. |
| **dst_len**          | Will be filled with the len of dst_data                                                                                              |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Please note that this function is for convenience, but should not be used
to resample audio in blocks, as it will introduce audio artifacts on the
boundaries. You should only use this function if you are converting audio
data in its entirety in one call. If you want to convert audio in smaller
chunks, use an [SDL_AudioStream](SDL_AudioStream), which is designed for
this situation.

Internally, this function creates and destroys an
[SDL_AudioStream](SDL_AudioStream) on each use, so it's also less efficient
than using one directly, if you need to convert multiple times.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateAudioStream](SDL_CreateAudioStream)

----
[CategoryAPI](CategoryAPI)

