###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamFormat

Change the input and output formats of an audio stream.

## Syntax

```c
int SDL_SetAudioStreamFormat(SDL_AudioStream *stream,
                             SDL_AudioFormat src_format,
                             int src_channels,
                             int src_rate,
                             SDL_AudioFormat dst_format,
                             int dst_channels,
                             int dst_rate);

```

## Function Parameters

|                      |                                                    |
| -------------------- | -------------------------------------------------- |
| **stream**           | The stream the format is being changed             |
| **src_format**       | The format of the audio input                      |
| **src_channels**     | The number of channels of the audio input          |
| **src_rate**         | The sampling rate of the audio input               |
| **dst_format**       | The format of the desired audio output             |
| **dst_channels**     | The number of channels of the desired audio output |
| **dst_rate**         | The sampling rate of the desired audio output      |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

Future calls to and
[SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable) and
[SDL_GetAudioStreamData](SDL_GetAudioStreamData) will reflect the new
format, and future calls to
[SDL_PutAudioStreamData](SDL_PutAudioStreamData) must provide data in the
new input formats.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAudioStreamFormat](SDL_GetAudioStreamFormat)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)

----
[CategoryAPI](CategoryAPI)

