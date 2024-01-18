###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetHapticGain

Set the global gain of the specified haptic device.

## Syntax

```c
int SDL_SetHapticGain(SDL_Haptic *haptic, int gain);

```

## Function Parameters

|                |                                                                 |
| -------------- | --------------------------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to set the gain on          |
| **gain**       | value to set the gain to, should be between 0 and 100 (0 - 100) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Device must support the [SDL_HAPTIC_GAIN](SDL_HAPTIC_GAIN) feature.

The user may specify the maximum gain by setting the environment variable
[`SDL_HAPTIC_GAIN_MAX`](SDL_HAPTIC_GAIN_MAX) which should be between 0 and
100. All calls to [SDL_SetHapticGain](SDL_SetHapticGain)() will scale
linearly using [`SDL_HAPTIC_GAIN_MAX`](SDL_HAPTIC_GAIN_MAX) as the maximum.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI)

