###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_MSToFrames

Convert milliseconds to sample frames at a specific sample rate.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Uint64 MIX_MSToFrames(int sample_rate, Uint64 ms);
```

## Function Parameters

|        |                 |                                                             |
| ------ | --------------- | ----------------------------------------------------------- |
| int    | **sample_rate** | the sample rate to use for conversion.                      |
| Uint64 | **ms**          | the milliseconds to convert to rate-specific sample frames. |

## Return Value

(Uint64) Returns Converted number of sample frames, or zero for errors.

## Remarks

If `sample_rate` is <= 0, this returns 0. No error is set.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_FramesToMS](MIX_FramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

