###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadButtonLabelForType

Get the label of a button on a gamepad.

## Syntax

```c
SDL_GamepadButtonLabel SDL_GetGamepadButtonLabelForType(SDL_GamepadType type, SDL_GamepadButton button);

```

## Function Parameters

|                |                                                                           |
| -------------- | ------------------------------------------------------------------------- |
| **type**       | the type of gamepad to check                                              |
| **button**     | a button index (one of the [SDL_GamepadButton](SDL_GamepadButton) values) |

## Return Value

Returns the [SDL_GamepadButtonLabel](SDL_GamepadButtonLabel) enum
corresponding to the button label

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadButtonLabel](SDL_GetGamepadButtonLabel)

----
[CategoryAPI](CategoryAPI)

