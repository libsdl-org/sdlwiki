###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickSetVirtualAxis

Set values on an opened, virtual-joystick's axis.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_JoystickSetVirtualAxis(SDL_Joystick *joystick, int axis, Sint16 value);

```

## Function Parameters

|                  |                                                   |
| ---------------- | ------------------------------------------------- |
| **joystick**     | the virtual joystick on which to set state.       |
| **axis**         | the specific axis on the virtual joystick to set. |
| **value**        | the new value for the specified axis.             |

## Return Value

Returns 0 on success, -1 on error.

## Remarks

Please note that values set here will not be applied until the next call to
[SDL_JoystickUpdate](SDL_JoystickUpdate), which can either be called
directly, or can be called indirectly through various other SDL APIs,
including, but not limited to the following:
[SDL_PollEvent](SDL_PollEvent), [SDL_PumpEvents](SDL_PumpEvents),
[SDL_WaitEventTimeout](SDL_WaitEventTimeout),
[SDL_WaitEvent](SDL_WaitEvent).

Note that when sending trigger axes, you should scale the value to the full
range of Sint16. For example, a trigger at rest would have the value of
[`SDL_JOYSTICK_AXIS_MIN`](SDL_JOYSTICK_AXIS_MIN).

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

