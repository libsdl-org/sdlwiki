###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PlayHapticRumble

Run a simple rumble effect on a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
bool SDL_PlayHapticRumble(SDL_Haptic *haptic, float strength, Uint32 length);
```

## Function Parameters

|                            |              |                                                      |
| -------------------------- | ------------ | ---------------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic**   | the haptic device to play the rumble effect on.      |
| float                      | **strength** | strength of the rumble to play as a 0-1 float value. |
| Uint32                     | **length**   | length of the rumble to play in milliseconds.        |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_InitHapticRumble](SDL_InitHapticRumble)
- [SDL_StopHapticRumble](SDL_StopHapticRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

