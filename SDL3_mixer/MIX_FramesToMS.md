###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_FramesToMS

Convert sample frames, at a specific sample rate, to milliseconds.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Uint64 MIX_FramesToMS(int sample_rate, Uint64 frames);
```

## Function Parameters

|        |                 |                                                             |
| ------ | --------------- | ----------------------------------------------------------- |
| int    | **sample_rate** | the sample rate to use for conversion.                      |
| Uint64 | **frames**      | the rate-specific sample frames to convert to milliseconds. |

## Return Value

(Uint64) Returns Converted number of milliseconds, or zero for errors.

## Remarks

If `sample_rate` is <= 0, this returns 0. No error is set.

Sample frames are more precise than milliseconds, so out of necessity, this
function will approximate by rounding down to the closest full millisecond.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_MSToFrames](MIX_MSToFrames)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

