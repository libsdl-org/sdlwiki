###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_VirtualJoystickDesc

The structure that describes a virtual joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
typedef struct SDL_VirtualJoystickDesc
{
    Uint16 type;        /**< `SDL_JoystickType` */
    Uint16 padding;     /**< unused */
    Uint16 vendor_id;   /**< the USB vendor ID of this joystick */
    Uint16 product_id;  /**< the USB product ID of this joystick */
    Uint16 naxes;       /**< the number of axes on this joystick */
    Uint16 nbuttons;    /**< the number of buttons on this joystick */
    Uint16 nballs;      /**< the number of balls on this joystick */
    Uint16 nhats;       /**< the number of hats on this joystick */
    Uint16 ntouchpads;  /**< the number of touchpads on this joystick, requires `touchpads` to point at valid descriptions */
    Uint16 nsensors;    /**< the number of sensors on this joystick, requires `sensors` to point at valid descriptions */
    Uint16 padding2[2]; /**< unused */
    Uint32 button_mask; /**< A mask of which buttons are valid for this controller
                             e.g. (1 << SDL_GAMEPAD_BUTTON_SOUTH) */
    Uint32 axis_mask;   /**< A mask of which axes are valid for this controller
                             e.g. (1 << SDL_GAMEPAD_AXIS_LEFTX) */
    const char *name;   /**< the name of the joystick */
    const SDL_VirtualJoystickTouchpadDesc *touchpads;   /**< A pointer to an array of touchpad descriptions, required if `ntouchpads` is > 0 */
    const SDL_VirtualJoystickSensorDesc *sensors;       /**< A pointer to an array of sensor descriptions, required if `nsensors` is > 0 */

    void *userdata;     /**< User data pointer passed to callbacks */
    void (SDLCALL *Update)(void *userdata); /**< Called when the joystick state should be updated */
    void (SDLCALL *SetPlayerIndex)(void *userdata, int player_index); /**< Called when the player index is set */
    int (SDLCALL *Rumble)(void *userdata, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble); /**< Implements SDL_RumbleJoystick() */
    int (SDLCALL *RumbleTriggers)(void *userdata, Uint16 left_rumble, Uint16 right_rumble); /**< Implements SDL_RumbleJoystickTriggers() */
    int (SDLCALL *SetLED)(void *userdata, Uint8 red, Uint8 green, Uint8 blue); /**< Implements SDL_SetJoystickLED() */
    int (SDLCALL *SendEffect)(void *userdata, const void *data, int size); /**< Implements SDL_SendJoystickEffect() */
    int (SDLCALL *SetSensorsEnabled)(void *userdata, SDL_bool enabled); /**< Implements SDL_SetGamepadSensorEnabled() */
} SDL_VirtualJoystickDesc;
```

## Remarks

All elements of this structure are optional and can be left 0.

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_AttachVirtualJoystick](SDL_AttachVirtualJoystick)
- [SDL_VirtualJoystickSensorDesc](SDL_VirtualJoystickSensorDesc)
- [SDL_VirtualJoystickTouchpadDesc](SDL_VirtualJoystickTouchpadDesc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryJoystick](CategoryJoystick)

