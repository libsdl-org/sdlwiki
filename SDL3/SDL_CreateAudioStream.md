# SDL_CreateAudioStream

Create a new audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_AudioStream * SDL_CreateAudioStream(const SDL_AudioSpec *src_spec, const SDL_AudioSpec *dst_spec);
```

## Function Parameters

|                                        |              |                                                      |
| -------------------------------------- | ------------ | ---------------------------------------------------- |
| const [SDL_AudioSpec](SDL_AudioSpec) * | **src_spec** | the format details of the input audio. May be NULL.  |
| const [SDL_AudioSpec](SDL_AudioSpec) * | **dst_spec** | the format details of the output audio. May be NULL. |

## Return Value

([SDL_AudioStream](SDL_AudioStream) *) Returns a new audio stream on
success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Note that `src_spec` or `dst_spec` may be NULL, but any attempts to put or
get data from an audio stream will fail until it has valid specs assigned
to both ends of the stream. Specs can be assigned later through
[SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat)(), or binding the
stream to an audio device (which will set the format of only the input or
output, depending on what kind of device the stream was bound to).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PutAudioStreamData](SDL_PutAudioStreamData)
- [SDL_GetAudioStreamData](SDL_GetAudioStreamData)
- [SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable)
- [SDL_FlushAudioStream](SDL_FlushAudioStream)
- [SDL_ClearAudioStream](SDL_ClearAudioStream)
- [SDL_SetAudioStreamFormat](SDL_SetAudioStreamFormat)
- [SDL_DestroyAudioStream](SDL_DestroyAudioStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

