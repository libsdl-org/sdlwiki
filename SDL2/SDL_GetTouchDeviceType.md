# SDL_GetTouchDeviceType

Get the type of the given touch device.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h)

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

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

