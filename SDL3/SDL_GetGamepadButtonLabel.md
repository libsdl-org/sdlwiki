###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadButtonLabel

Get the label of a button on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_GamepadButtonLabel SDL_GetGamepadButtonLabel(SDL_Gamepad *gamepad, SDL_GamepadButton button);

```

## Function Parameters

|                 |                                                                           |
| --------------- | ------------------------------------------------------------------------- |
| **gamepad**     | a gamepad                                                                 |
| **button**      | a button index (one of the [SDL_GamepadButton](SDL_GamepadButton) values) |

## Return Value

Returns the [SDL_GamepadButtonLabel](SDL_GamepadButtonLabel) enum
corresponding to the button label

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadButtonLabelForType](SDL_GetGamepadButtonLabelForType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

