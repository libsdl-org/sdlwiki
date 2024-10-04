###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAudioFormatName

Get the human readable name of an audio format.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
const char * SDL_GetAudioFormatName(SDL_AudioFormat format);
```

## Function Parameters

|                                    |            |                            |
| ---------------------------------- | ---------- | -------------------------- |
| [SDL_AudioFormat](SDL_AudioFormat) | **format** | the audio format to query. |

## Return Value

(const char *) Returns the human readable name of the specified audio
format or "[SDL_AUDIO_UNKNOWN](SDL_AUDIO_UNKNOWN)" if the format isn't
recognized.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

