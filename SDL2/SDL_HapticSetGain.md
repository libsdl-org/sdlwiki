###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticSetGain

Set the global gain of the specified haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_HapticSetGain(SDL_Haptic * haptic, int gain);
```

## Function Parameters

|                            |            |                                                                 |
| -------------------------- | ---------- | --------------------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to set the gain on          |
| int                        | **gain**   | value to set the gain to, should be between 0 and 100 (0 - 100) |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the [SDL_HAPTIC_GAIN](SDL_HAPTIC_GAIN) feature.

The user may specify the maximum gain by setting the environment variable
[`SDL_HAPTIC_GAIN_MAX`](SDL_HAPTIC_GAIN_MAX) which should be between 0 and
100. All calls to [SDL_HapticSetGain](SDL_HapticSetGain)() will scale
linearly using [`SDL_HAPTIC_GAIN_MAX`](SDL_HAPTIC_GAIN_MAX) as the maximum.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_HapticQuery](SDL_HapticQuery)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

