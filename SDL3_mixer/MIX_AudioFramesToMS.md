###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_AudioFramesToMS

Convert sample frames for a [MIX_Audio](MIX_Audio)'s format to milliseconds.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_AudioFramesToMS(MIX_Audio *audio, Sint64 frames);
```

## Function Parameters

|                          |            |                                                              |
| ------------------------ | ---------- | ------------------------------------------------------------ |
| [MIX_Audio](MIX_Audio) * | **audio**  | the audio to query.                                          |
| Sint64                   | **frames** | the audio-specific sample frames to convert to milliseconds. |

## Return Value

(Sint64) Returns Converted number of milliseconds, or -1 for errors/no
input; call SDL_GetError() for details.

## Remarks

This calculates time based on the audio's initial format, even if the
format would change mid-stream.

Sample frames are more precise than milliseconds, so out of necessity, this
function will approximate by rounding down to the closest full millisecond.

If `frames` is < 0, this returns -1.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_AudioMSToFrames](MIX_AudioMSToFrames)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

