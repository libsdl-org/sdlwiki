###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoysticks

Get a list of currently connected joysticks.

## Syntax

```c
SDL_JoystickID* SDL_GetJoysticks(int *count);

```

## Function Parameters

|               |                                                           |
| ------------- | --------------------------------------------------------- |
| **count**     | a pointer filled in with the number of joysticks returned |

## Return Value

Returns a 0 terminated array of joystick instance IDs which should be freed
with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenJoystick](SDL_OpenJoystick)

----
[CategoryAPI](CategoryAPI)

