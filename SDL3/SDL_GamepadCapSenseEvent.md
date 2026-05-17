# SDL_GamepadCapSenseEvent

Gamepad capsense event structure (event.gcapsense.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_GamepadCapSenseEvent
{
    SDL_EventType type;     /**< SDL_EVENT_GAMEPAD_CAPSENSE_TOUCH or SDL_EVENT_GAMEPAD_CAPSENSE_RELEASE */
    Uint32 reserved;
    Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_JoystickID which;   /**< The joystick instance id */
    Uint8 capsense;         /**< The capsense type (SDL_GamepadCapSenseType) */
    bool down;              /**< true if the capsense is touched */
    Uint8 padding1;
    Uint8 padding2;
} SDL_GamepadCapSenseEvent;
```

## Version

This struct is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

