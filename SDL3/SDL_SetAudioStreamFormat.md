###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAudioStreamFormat

Change the input and output formats of an audio stream.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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

## See Also

* [SDL_GetAudioStreamFormat](SDL_GetAudioStreamFormat)
* [SDL_SetAudioStreamFrequencyRatio](SDL_SetAudioStreamFrequencyRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

