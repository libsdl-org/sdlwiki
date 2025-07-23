###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_AudioFramesToMS

Convert sample frames for a [MIX_Audio](MIX_Audio)'s format to milliseconds.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Uint64 MIX_AudioFramesToMS(MIX_Audio *audio, Uint64 frames);
```

## Function Parameters

|                          |            |                                                              |
| ------------------------ | ---------- | ------------------------------------------------------------ |
| [MIX_Audio](MIX_Audio) * | **audio**  | the audio to query.                                          |
| Uint64                   | **frames** | the audio-specific sample frames to convert to milliseconds. |

## Return Value

(Uint64) Returns Converted number of milliseconds, or zero for errors/no
input.

## Remarks

This calculates time based on the audio's initial format, even if the
format would change mid-stream.

Sample frames are more precise than milliseconds, so out of necessity, this
function will approximate by rounding down to the closest full millisecond.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_AudioMSToFrames](MIX_AudioMSToFrames)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

