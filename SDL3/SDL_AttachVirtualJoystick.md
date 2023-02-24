###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AttachVirtualJoystick

Attach a new virtual joystick.

## Syntax

```c
SDL_JoystickID SDL_AttachVirtualJoystick(SDL_JoystickType type,
                              int naxes,
                              int nbuttons,
                              int nhats);

```

## Function Parameters

|                  |                   |
| ---------------- | ----------------- |
| **type**         | type of joystick  |
| **naxes**        | number of axes    |
| **nbuttons**     | number of buttons |
| **nhats**        | number of hats    |

## Return Value

Returns the joystick instance ID, or 0 if an error occurred; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

