###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGamepadMapping

Set the current mapping of a joystick or gamepad.

## Syntax

```c
int SDL_SetGamepadMapping(SDL_JoystickID instance_id, const char *mapping);

```

## Function Parameters

|                     |                                                                  |
| ------------------- | ---------------------------------------------------------------- |
| **instance_id**     | the joystick instance ID                                         |
| **mapping**         | the mapping to use for this device, or NULL to clear the mapping |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Details about mappings are discussed with
[SDL_AddGamepadMapping](SDL_AddGamepadMapping)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AddGamepadMapping](SDL_AddGamepadMapping)
* [SDL_GetGamepadMapping](SDL_GetGamepadMapping)

----
[CategoryAPI](CategoryAPI)

