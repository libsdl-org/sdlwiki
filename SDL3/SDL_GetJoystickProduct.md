###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickProduct

Get the USB product ID of an opened joystick, if available.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
Uint16 SDL_GetJoystickProduct(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                                        |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)(). |

## Return Value

(Uint16) Returns the USB product ID of the selected joystick, or 0 if
unavailable.

## Remarks

If the product ID isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickProductFromID](SDL_GetJoystickProductFromID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

