###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_OpenHapticFromMouse

Try to open a haptic device from the current mouse.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
SDL_Haptic * SDL_OpenHapticFromMouse(void);
```

## Return Value

([SDL_Haptic](SDL_Haptic) *) Returns the haptic device identifier or NULL
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_CloseHaptic](SDL_CloseHaptic)
- [SDL_IsMouseHaptic](SDL_IsMouseHaptic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

