###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetHapticNameForID

Get the implementation dependent name of a haptic device.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
const char * SDL_GetHapticNameForID(SDL_HapticID instance_id);
```

## Function Parameters

|                              |                 |                                |
| ---------------------------- | --------------- | ------------------------------ |
| [SDL_HapticID](SDL_HapticID) | **instance_id** | the haptic device instance ID. |

## Return Value

(const char *) Returns the name of the selected haptic device. If no name
can be found, this function returns NULL; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This can be called before any haptic devices are opened.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetHapticName](SDL_GetHapticName)
- [SDL_OpenHaptic](SDL_OpenHaptic)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHaptic](CategoryHaptic)

