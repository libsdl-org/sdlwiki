###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_AudioMSToFrames

Convert milliseconds to sample frames for a [MIX_Audio](MIX_Audio)'s format.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Uint64 MIX_AudioMSToFrames(MIX_Audio *audio, Uint64 ms);
```

## Function Parameters

|                          |           |                                                              |
| ------------------------ | --------- | ------------------------------------------------------------ |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio to query.                                          |
| Uint64                   | **ms**    | the milliseconds to convert to audio-specific sample frames. |

## Return Value

(Uint64) Returns Converted number of sample frames, or zero for errors/no
input.

## Remarks

This calculates time based on the audio's initial format, even if the
format would change mid-stream.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_AudioFramesToMS](MIX_AudioFramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

