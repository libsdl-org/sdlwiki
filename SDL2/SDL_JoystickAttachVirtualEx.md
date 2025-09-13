# SDL_JoystickAttachVirtualEx

Attach a new virtual joystick with extended properties.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickAttachVirtualEx(const SDL_VirtualJoystickDesc *desc);
```

## Function Parameters

|                                                            |          |                       |
| ---------------------------------------------------------- | -------- | --------------------- |
| const [SDL_VirtualJoystickDesc](SDL_VirtualJoystickDesc) * | **desc** | joystick description. |

## Return Value

(int) Returns the joystick's device index, or -1 if an error occurred.

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

