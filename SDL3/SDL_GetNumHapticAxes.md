###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumHapticAxes

Get the number of haptic axes the device has.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
int SDL_GetNumHapticAxes(SDL_Haptic *haptic);
```

## Function Parameters

|                            |            |                                               |
| -------------------------- | ---------- | --------------------------------------------- |
| [SDL_Haptic](SDL_Haptic) * | **haptic** | the [SDL_Haptic](SDL_Haptic) device to query. |

## Return Value

(int) Returns the number of axes on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The number of haptic axes might be useful if working with the
[SDL_HapticDirection](SDL_HapticDirection) effect.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

