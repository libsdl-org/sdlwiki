###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetHapticAutocenter

Set the global autocenter of the device.

## Syntax

```c
int SDL_SetHapticAutocenter(SDL_Haptic *haptic, int autocenter);

```

## Function Parameters

|                    |                                                             |
| ------------------ | ----------------------------------------------------------- |
| **haptic**         | the [SDL_Haptic](SDL_Haptic) device to set autocentering on |
| **autocenter**     | value to set autocenter to (0-100)                          |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Autocenter should be between 0 and 100. Setting it to 0 will disable
autocentering.

Device must support the [SDL_HAPTIC_AUTOCENTER](SDL_HAPTIC_AUTOCENTER)
feature.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetHapticFeatures](SDL_GetHapticFeatures)

----
[CategoryAPI](CategoryAPI)

