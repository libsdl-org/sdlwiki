###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamFormat

Change the input and output formats of an audio stream.

## Syntax

```c
int SDL_SetAudioStreamFormat(SDL_AudioStream *stream,
                             const SDL_AudioSpec *src_spec,
                             const SDL_AudioSpec *dst_spec);

```

## Function Parameters

|                  |                                                                 |
| ---------------- | --------------------------------------------------------------- |
| **stream**       | The stream the format is being changed                          |
| **src_spec**     | The new format of the audio input; if NULL, it is not changed.  |
| **dst_spec**     | The new format of the audio output; if NULL, it is not changed. |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

Future calls to and
[SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable.md) and
[SDL_GetAudioStreamData](SDL_GetAudioStreamData.md) will reflect the new
format, and future calls to
[SDL_PutAudioStreamData](SDL_PutAudioStreamData.md) must provide data in the
new input formats.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetAudioStreamFormat](SDL_GetAudioStreamFormat.md)
* [SDL_PutAudioStreamData](SDL_PutAudioStreamData.md)
* [SDL_GetAudioStreamData](SDL_GetAudioStreamData.md)
* [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable.md)
* [SDL_SetAudioStreamFrequencyRatio](SDL_SetAudioStreamFrequencyRatio.md)

----
[CategoryAPI](CategoryAPI.md)
