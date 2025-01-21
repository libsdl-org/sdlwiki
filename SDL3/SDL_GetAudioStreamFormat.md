###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAudioStreamFormat

Query the current format of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_GetAudioStreamFormat(SDL_AudioStream *stream, SDL_AudioSpec *src_spec, SDL_AudioSpec *dst_spec);
```

## Function Parameters

|                                      |              |                                                          |
| ------------------------------------ | ------------ | -------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) * | **stream**   | the [SDL_AudioStream](SDL_AudioStream) to query.         |
| [SDL_AudioSpec](SDL_AudioSpec) *     | **src_spec** | where to store the input audio format; ignored if NULL.  |
| [SDL_AudioSpec](SDL_AudioSpec) *     | **dst_spec** | where to store the output audio format; ignored if NULL. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

