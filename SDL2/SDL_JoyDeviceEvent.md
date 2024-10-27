###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_JoyDeviceEvent

Joystick device event structure (event.jdevice.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyDeviceEvent
{
    Uint32 type;        /**< SDL_JOYDEVICEADDED or SDL_JOYDEVICEREMOVED */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Sint32 which;       /**< The joystick device index for the ADDED event, instance id for the REMOVED event */
} SDL_JoyDeviceEvent;
```

## Remarks

SDL will send JOYSTICK_ADDED events for devices that are already plugged in
during [SDL_Init](SDL_Init).

## See Also

- [SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

