###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_MSToFrames

Convert milliseconds to sample frames at a specific sample rate.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Sint64 MIX_MSToFrames(int sample_rate, Sint64 ms);
```

## Function Parameters

|        |                 |                                                             |
| ------ | --------------- | ----------------------------------------------------------- |
| int    | **sample_rate** | the sample rate to use for conversion.                      |
| Sint64 | **ms**          | the milliseconds to convert to rate-specific sample frames. |

## Return Value

(Sint64) Returns Converted number of sample frames, or -1 for errors; call
SDL_GetError() for details.

## Remarks

If `sample_rate` is <= 0, this returns -1. If `ms` is < 0, this returns -1.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_FramesToMS](MIX_FramesToMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

