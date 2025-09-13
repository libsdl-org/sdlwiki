# SDL_JoystickAttachVirtual

Attach a new virtual joystick.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickAttachVirtual(SDL_JoystickType type,
                              int naxes,
                              int nbuttons,
                              int nhats);
```

## Function Parameters

|                                      |              |                    |
| ------------------------------------ | ------------ | ------------------ |
| [SDL_JoystickType](SDL_JoystickType) | **type**     | joystick type.     |
| int                                  | **naxes**    | number of axes.    |
| int                                  | **nbuttons** | number of buttons. |
| int                                  | **nhats**    | number of hats.    |

## Return Value

(int) Returns the joystick's device index, or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

