###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGamepadMappingForID

Get the mapping of a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
char * SDL_GetGamepadMappingForID(SDL_JoystickID instance_id);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID. |

## Return Value

(char *) Returns the mapping string. Returns NULL if no mapping is
available. This should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Remarks

This can be called before any gamepads are opened.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepads](SDL_GetGamepads)
- [SDL_GetGamepadMapping](SDL_GetGamepadMapping)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

