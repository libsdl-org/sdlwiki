# SDL_JoyDeviceEvent

Joystick device event structure (event.jdevice.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyDeviceEvent
{
    SDL_EventType type; /**< SDL_EVENT_JOYSTICK_ADDED or SDL_EVENT_JOYSTICK_REMOVED or SDL_EVENT_JOYSTICK_UPDATE_COMPLETE */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_JoystickID which;       /**< The joystick instance id */
} SDL_JoyDeviceEvent;
```

## Remarks

SDL will send JOYSTICK_ADDED events for devices that are already plugged in
during [SDL_Init](SDL_Init).

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

