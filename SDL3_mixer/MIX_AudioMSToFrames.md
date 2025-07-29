###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_AudioMSToFrames

Convert milliseconds to sample frames for a [MIX_Audio](MIX_Audio)'s format.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_AudioMSToFrames(MIX_Audio *audio, Sint64 ms);
```

## Function Parameters

|                          |           |                                                              |
| ------------------------ | --------- | ------------------------------------------------------------ |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio to query.                                          |
| Sint64                   | **ms**    | the milliseconds to convert to audio-specific sample frames. |

## Return Value

(Sint64) Returns Converted number of sample frames, or -1 for errors/no
input; call SDL_GetError() for details.

## Remarks

This calculates time based on the audio's initial format, even if the
format would change mid-stream.

If `ms` is < 0, this returns -1.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_AudioFramesToMS](MIX_AudioFramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

