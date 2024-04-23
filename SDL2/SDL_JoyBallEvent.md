###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoyBallEvent

Joystick trackball motion event structure (event.jball.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyBallEvent
{
    Uint32 type;        /**< ::SDL_JOYBALLMOTION */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 ball;         /**< The joystick trackball index */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 xrel;        /**< The relative motion in the X direction */
    Sint16 yrel;        /**< The relative motion in the Y direction */
} SDL_JoyBallEvent;
```

## Data Fields

|                |               |                                                         |
| -------------- | ------------- | ------------------------------------------------------- |
| Uint32         | **type**      | SDL_JOYBALLMOTION                                       |
| Uint32         | **timestamp** | timestamp of the event                                  |
| SDL_JoystickID | **which**     | the instance id of the joystick that reported the event |
| Uint8          | **ball**      | the index of the trackball that changed                 |
| Sint16         | **xrel**      | the relative motion in the X direction                  |
| Sint16         | **yrel**      | the relative motion in the Y direction                  |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_JoyAxisEvent](SDL_JoyAxisEvent)
[SDL_JoyButtonEvent](SDL_JoyButtonEvent)
[SDL_JoyHatEvent](SDL_JoyHatEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


