###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickVirtualAxis

Set values on an opened, virtual-joystick's axis.

## Syntax

```c
int SDL_SetJoystickVirtualAxis(SDL_Joystick *joystick, int axis, Sint16 value);

```

## Function Parameters

|                  |                                                   |
| ---------------- | ------------------------------------------------- |
| **joystick**     | the virtual joystick on which to set state.       |
| **axis**         | the specific axis on the virtual joystick to set. |
| **value**        | the new value for the specified axis.             |

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

Note that when sending trigger axes, you should scale the value to the full
range of Sint16. For example, a trigger at rest would have the value of
[`SDL_JOYSTICK_AXIS_MIN`](SDL_JOYSTICK_AXIS_MIN).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

