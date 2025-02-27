# SDL_VirtualJoystickDesc

The structure that defines an extended virtual joystick description

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
typedef struct SDL_VirtualJoystickDesc
{
    Uint16 version;     /**< `SDL_VIRTUAL_JOYSTICK_DESC_VERSION` */
    Uint16 type;        /**< `SDL_JoystickType` */
    Uint16 naxes;       /**< the number of axes on this joystick */
    Uint16 nbuttons;    /**< the number of buttons on this joystick */
    Uint16 nhats;       /**< the number of hats on this joystick */
    Uint16 vendor_id;   /**< the USB vendor ID of this joystick */
    Uint16 product_id;  /**< the USB product ID of this joystick */
    Uint16 padding;     /**< unused */
    Uint32 button_mask; /**< A mask of which buttons are valid for this controller
                             e.g. (1 << SDL_CONTROLLER_BUTTON_A) */
    Uint32 axis_mask;   /**< A mask of which axes are valid for this controller
                             e.g. (1 << SDL_CONTROLLER_AXIS_LEFTX) */
    const char *name;   /**< the name of the joystick */

    void *userdata;     /**< User data pointer passed to callbacks */
    void (SDLCALL *Update)(void *userdata); /**< Called when the joystick state should be updated */
    void (SDLCALL *SetPlayerIndex)(void *userdata, int player_index); /**< Called when the player index is set */
    int (SDLCALL *Rumble)(void *userdata, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble); /**< Implements SDL_JoystickRumble() */
    int (SDLCALL *RumbleTriggers)(void *userdata, Uint16 left_rumble, Uint16 right_rumble); /**< Implements SDL_JoystickRumbleTriggers() */
    int (SDLCALL *SetLED)(void *userdata, Uint8 red, Uint8 green, Uint8 blue); /**< Implements SDL_JoystickSetLED() */
    int (SDLCALL *SendEffect)(void *userdata, const void *data, int size); /**< Implements SDL_JoystickSendEffect() */

} SDL_VirtualJoystickDesc;
```

## Remarks

The caller must zero the structure and then initialize the version with
[`SDL_VIRTUAL_JOYSTICK_DESC_VERSION`](SDL_VIRTUAL_JOYSTICK_DESC_VERSION)
before passing it to
[SDL_JoystickAttachVirtualEx](SDL_JoystickAttachVirtualEx)() All other
elements of this structure are optional and can be left 0.

## See Also

- [SDL_JoystickAttachVirtualEx](SDL_JoystickAttachVirtualEx)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryJoystick](CategoryJoystick)

