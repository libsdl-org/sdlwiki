###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGamepadMapping

Set the current mapping of a joystick or gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_bool SDL_SetGamepadMapping(SDL_JoystickID instance_id, const char *mapping);
```

## Function Parameters

|                                  |                 |                                                                   |
| -------------------------------- | --------------- | ----------------------------------------------------------------- |
| [SDL_JoystickID](SDL_JoystickID) | **instance_id** | the joystick instance ID.                                         |
| const char *                     | **mapping**     | the mapping to use for this device, or NULL to clear the mapping. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Details about mappings are discussed with
[SDL_AddGamepadMapping](SDL_AddGamepadMapping)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AddGamepadMapping](SDL_AddGamepadMapping)
- [SDL_GetGamepadMapping](SDL_GetGamepadMapping)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

