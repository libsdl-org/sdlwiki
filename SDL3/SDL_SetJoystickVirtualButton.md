###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickVirtualButton

Set values on an opened, virtual-joystick's button.

## Syntax

```c
int SDL_SetJoystickVirtualButton(SDL_Joystick *joystick, int button, Uint8 value);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **joystick**     | the virtual joystick on which to set state.         |
| **button**       | the specific button on the virtual joystick to set. |
| **value**        | the new value for the specified button.             |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Please note that values set here will not be applied until the next call to
[SDL_UpdateJoysticks](SDL_UpdateJoysticks), which can either be called
directly, or can be called indirectly through various other SDL APIs,
including, but not limited to the following:
[SDL_PollEvent](SDL_PollEvent), [SDL_PumpEvents](SDL_PumpEvents),
[SDL_WaitEventTimeout](SDL_WaitEventTimeout),
[SDL_WaitEvent](SDL_WaitEvent).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

