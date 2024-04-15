###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_JoyAxisEvent

Joystick axis motion event structure (event.jaxis.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_JoyAxisEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_JOYSTICK_AXIS_MOTION */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 axis;         /**< The joystick axis index */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;       /**< The axis value (range: -32768 to 32767) */
    Uint16 padding4;
} SDL_JoyAxisEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

