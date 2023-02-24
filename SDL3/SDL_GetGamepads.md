###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepads

Get a list of currently connected gamepads.

## Syntax

```c
SDL_JoystickID* SDL_GetGamepads(int *count);

```

## Function Parameters

|               |                                                          |
| ------------- | -------------------------------------------------------- |
| **count**     | a pointer filled in with the number of gamepads returned |

## Return Value

Returns a 0 terminated array of joystick instance IDs which should be freed
with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

