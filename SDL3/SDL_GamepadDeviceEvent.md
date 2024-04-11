###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadDeviceEvent

Gamepad device event structure (event.gdevice.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_GamepadDeviceEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_GAMEPAD_ADDED, ::SDL_EVENT_GAMEPAD_REMOVED, or ::SDL_EVENT_GAMEPAD_REMAPPED, ::SDL_EVENT_GAMEPAD_UPDATE_COMPLETE or ::SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_JoystickID which;       /**< The joystick instance id */
} SDL_GamepadDeviceEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

