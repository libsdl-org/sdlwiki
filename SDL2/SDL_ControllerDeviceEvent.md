# SDL_ControllerDeviceEvent

Controller device event structure (event.cdevice.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_ControllerDeviceEvent
{
    Uint32 type;        /**< SDL_CONTROLLERDEVICEADDED, SDL_CONTROLLERDEVICEREMOVED, SDL_CONTROLLERDEVICEREMAPPED, or SDL_CONTROLLERSTEAMHANDLEUPDATED */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Sint32 which;       /**< The joystick device index for the ADDED event, instance id for the REMOVED or REMAPPED event */
} SDL_ControllerDeviceEvent;
```

## Remarks

Joysticks that are supported game controllers receive both an
[SDL_JoyDeviceEvent](SDL_JoyDeviceEvent) and an
[SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent).

SDL will send CONTROLLERDEVICEADDED events for joysticks that are already
plugged in during [SDL_Init](SDL_Init)() and are recognized as game
controllers.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

