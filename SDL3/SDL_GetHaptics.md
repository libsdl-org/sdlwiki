###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetHaptics

Get a list of currently connected haptic devices.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_HapticID * SDL_GetHaptics(int *count);
```

## Function Parameters

|       |           |                                                                              |
| ----- | --------- | ---------------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of haptic devices returned, may be NULL. |

## Return Value

([SDL_HapticID](SDL_HapticID) *) Returns a 0 terminated array of haptic
device instance IDs or NULL on failure; call [SDL_GetError](SDL_GetError)()
for more information. This should be freed with [SDL_free](SDL_free)() when
it is no longer needed.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_OpenHaptic](SDL_OpenHaptic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

