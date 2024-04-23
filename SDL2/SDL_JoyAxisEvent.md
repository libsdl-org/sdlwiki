###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoyAxisEvent

Joystick axis motion event structure (event.jaxis.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyAxisEvent
{
    Uint32 type;        /**< ::SDL_JOYAXISMOTION */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 axis;         /**< The joystick axis index */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;       /**< The axis value (range: -32768 to 32767) */
    Uint16 padding4;
} SDL_JoyAxisEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_JOYAXISMOTION
|-
|Uint32
|'''timestamp'''
|timestamp of the event
|-
|SDL_JoystickID
|'''which'''
|the instance id of the joystick that reported the event
|-
|Uint8
|'''axis'''
|the index of the axis that changed
|-
|Sint16
|'''value'''
|the current position of the axis (range: -32768 to 32767)
|}

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_JoyBallEvent](SDL_JoyBallEvent)
[SDL_JoyButtonEvent](SDL_JoyButtonEvent)
[SDL_JoyHatEvent](SDL_JoyHatEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


