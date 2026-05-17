# SDL_GamepadCapSenseType

The list of capsense types on a gamepad

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
typedef enum SDL_GamepadCapSenseType
{
    SDL_GAMEPAD_CAPSENSE_INVALID = -1,
    SDL_GAMEPAD_CAPSENSE_LEFT_STICK,    /**< Activated by touching the top of the left thumbstick */
    SDL_GAMEPAD_CAPSENSE_RIGHT_STICK,   /**< Activated by touching the top of the right thumbstick */
    SDL_GAMEPAD_CAPSENSE_LEFT_GRIP,     /**< Activated by gripping the left handle of the controller */
    SDL_GAMEPAD_CAPSENSE_RIGHT_GRIP,    /**< Activated by gripping the right handle of the controller */
    SDL_GAMEPAD_CAPSENSE_COUNT
} SDL_GamepadCapSenseType;
```

## Version

This enum is available since SDL 3.6.0.

## See Also

- [SDL_GamepadHasCapSense](SDL_GamepadHasCapSense)
- [SDL_GetGamepadCapSense](SDL_GetGamepadCapSense)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGamepad](CategoryGamepad)

