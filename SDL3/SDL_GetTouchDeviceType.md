###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTouchDeviceType

Get the type of the given touch device.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
SDL_TouchDeviceType SDL_GetTouchDeviceType(SDL_TouchID touchID);
```

## Function Parameters

|                            |             |                           |
| -------------------------- | ----------- | ------------------------- |
| [SDL_TouchID](SDL_TouchID) | **touchID** | the ID of a touch device. |

## Return Value

([SDL_TouchDeviceType](SDL_TouchDeviceType)) Returns touch device type.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

