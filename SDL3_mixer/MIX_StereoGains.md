###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_StereoGains

A set of per-channel gains for tracks using [MIX_SetTrackStereo](MIX_SetTrackStereo)().

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef struct MIX_StereoGains
{
    float left;   /**< left channel gain */
    float right;  /**< right channel gain */
} MIX_StereoGains;
```

## Remarks

When forcing a track to stereo, the app can specify a per-channel gain, to
further adjust the left or right outputs.

When mixing audio that has been forced to stereo, each channel is modulated
by these values. A value of 1.0f produces no change, 0.0f produces silence.

A simple panning effect would be to set `left` to the desired value and
`right` to `1.0f - left`.

## Version

This struct is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrackStereo](MIX_SetTrackStereo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLMixer](CategorySDLMixer)

