# SDL_HapticRumblePlay

Run a simple rumble effect on a haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
int SDL_HapticRumblePlay(SDL_Haptic * haptic, float strength, Uint32 length );
```

## Function Parameters

|                            |              |                                                      |
| -------------------------- | ------------ | ---------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic**   | the haptic device to play the rumble effect on.      |
| float                      | **strength** | strength of the rumble to play as a 0-1 float value. |
| [Uint32](Uint32)           | **length**   | length of the rumble to play in milliseconds.        |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_HapticRumbleInit](SDL_HapticRumbleInit)
- [SDL_HapticRumbleStop](SDL_HapticRumbleStop)
- [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

