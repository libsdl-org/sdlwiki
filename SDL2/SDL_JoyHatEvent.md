###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoyHatEvent

Joystick hat position change event structure (event.jhat.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyHatEvent
{
    Uint32 type;        /**< ::SDL_JOYHATMOTION */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 hat;          /**< The joystick hat index */
    Uint8 value;        /**< The hat position value.
                         *   \sa ::SDL_HAT_LEFTUP ::SDL_HAT_UP ::SDL_HAT_RIGHTUP
                         *   \sa ::SDL_HAT_LEFT ::SDL_HAT_CENTERED ::SDL_HAT_RIGHT
                         *   \sa ::SDL_HAT_LEFTDOWN ::SDL_HAT_DOWN ::SDL_HAT_RIGHTDOWN
                         *
                         *   Note that zero means the POV is centered.
                         */
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyHatEvent;
```

## Data Fields

|                |                 |                                                         |
| -------------- | --------------- | ------------------------------------------------------- |
| Uint32         | '''type'''      | SDL_JOYHATMOTION                                        |
| Uint32         | '''timestamp''' | timestamp of the event                                  |
| SDL_JoystickID | '''which'''     | the instance id of the joystick that reported the event |
| Uint8          | '''hat'''       | the index of the hat that changed                       |
| Uint8          | '''value'''     | the new position of the hat; see Remarks for details    |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_JoyAxisEvent](SDL_JoyAxisEvent)
[SDL_JoyBallEvent](SDL_JoyBallEvent)
[SDL_JoyButtonEvent](SDL_JoyButtonEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


