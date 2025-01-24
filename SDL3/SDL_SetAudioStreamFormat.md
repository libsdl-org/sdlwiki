# SDL_SetAudioStreamFormat

Change the input and output formats of an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_SetAudioStreamFormat(SDL_AudioStream *stream, const SDL_AudioSpec *src_spec, const SDL_AudioSpec *dst_spec);
```

## Function Parameters

|                                        |              |                                                                 |
| -------------------------------------- | ------------ | --------------------------------------------------------------- |
| [SDL_AudioStream](SDL_AudioStream) *   | **stream**   | the stream the format is being changed.                         |
| const [SDL_AudioSpec](SDL_AudioSpec) * | **src_spec** | the new format of the audio input; if NULL, it is not changed.  |
| const [SDL_AudioSpec](SDL_AudioSpec) * | **dst_spec** | the new format of the audio output; if NULL, it is not changed. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Future calls to and
[SDL_GetAudioStreamAvailable](SDL_GetAudioStreamAvailable) and
[SDL_GetAudioStreamData](SDL_GetAudioStreamData) will reflect the new
format, and future calls to
[SDL_PutAudioStreamData](SDL_PutAudioStreamData) must provide data in the
new input formats.

Data that was previously queued in the stream will still be operated on in
the format that was current when it was added, which is to say you can put
the end of a sound file in one format to a stream, change formats for the
next sound file, and start putting that new data while the previous sound
file is still queued, and everything will still play back correctly.

If a stream is bound to a device, then the format of the side of the stream
bound to a device cannot be changed (src_spec for recording devices,
dst_spec for playback devices). Attempts to make a change to this side will
be ignored, but this will not report an error. The other side's format can
be changed.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAudioStreamFormat](SDL_GetAudioStreamFormat)
- [SDL_SetAudioStreamFrequencyRatio](SDL_SetAudioStreamFrequencyRatio)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

