###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_JoyButtonEvent

Joystick button event structure (event.jbutton.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyButtonEvent
{
    SDL_EventType type; /**< SDL_EVENT_JOYSTICK_BUTTON_DOWN or SDL_EVENT_JOYSTICK_BUTTON_UP */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 button;       /**< The joystick button index */
    bool down;      /**< true if the button is pressed */
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyButtonEvent;
```

## Version

This struct is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

