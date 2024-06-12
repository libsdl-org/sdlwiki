###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetJoystickVirtualTouchpad

Set touchpad finger state on an opened virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
int SDL_SetJoystickVirtualTouchpad(SDL_Joystick *joystick, int touchpad, int finger, Uint8 state, float x, float y, float pressure);
```

## Function Parameters

|                                |              |                                                                                                                 |
| ------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the virtual joystick on which to set state.                                                                     |
| int                            | **touchpad** | the index of the touchpad on the virtual joystick to update.                                                    |
| int                            | **finger**   | the index of the finger on the touchpad to set.                                                                 |
| Uint8                          | **state**    | [`SDL_PRESSED`](SDL_PRESSED) if the finger is pressed, [`SDL_RELEASED`](SDL_RELEASED) if the finger is released |
| float                          | **x**        | the x coordinate of the finger on the touchpad, normalized 0 to 1, with the origin in the upper left            |
| float                          | **y**        | the y coordinate of the finger on the touchpad, normalized 0 to 1, with the origin in the upper left            |
| float                          | **pressure** | the pressure of the finger                                                                                      |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
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
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

