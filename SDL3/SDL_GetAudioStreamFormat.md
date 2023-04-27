###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioStreamFormat

Query the current format of an audio stream.

## Syntax

```c
int SDL_GetAudioStreamFormat(SDL_AudioStream *stream,
                             SDL_AudioFormat *src_format,
                             int *src_channels,
                             int *src_rate,
                             SDL_AudioFormat *dst_format,
                             int *dst_channels,
                             int *dst_rate);

```

## Function Parameters

|                      |                                                           |
| -------------------- | --------------------------------------------------------- |
| **stream**           | the [SDL_AudioStream](SDL_AudioStream) to query.          |
| **src_format**       | Where to store the input audio format; ignored if NULL.   |
| **src_channels**     | Where to store the input channel count; ignored if NULL.  |
| **src_rate**         | Where to store the input sample rate; ignored if NULL.    |
| **dst_format**       | Where to store the output audio format; ignored if NULL.  |
| **dst_channels**     | Where to store the output channel count; ignored if NULL. |
| **dst_rate**         | Where to store the output sample rate; ignored if NULL.   |

## Return Value

Returns 0 on success, or -1 on error.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

