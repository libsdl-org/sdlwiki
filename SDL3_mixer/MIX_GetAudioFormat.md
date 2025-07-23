###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetAudioFormat

Query the initial audio format of a [MIX_Audio](MIX_Audio).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_GetAudioFormat(MIX_Audio *audio, SDL_AudioSpec *spec);
```

## Function Parameters

|                          |           |                                                       |
| ------------------------ | --------- | ----------------------------------------------------- |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio to query.                                   |
| SDL_AudioSpec *          | **spec**  | on success, audio format details will be stored here. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Note that some audio files can change format in the middle; some explicitly
support this, but a more common example is two MP3 files concatenated
together. In many cases, SDL_mixer will correctly handle these sort of
files, but this function will only report the initial format a file uses.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

