###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoyButtonEvent

Joystick button event structure (event.jbutton.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyButtonEvent
{
    Uint32 type;        /**< ::SDL_JOYBUTTONDOWN or ::SDL_JOYBUTTONUP */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 button;       /**< The joystick button index */
    Uint8 state;        /**< ::SDL_PRESSED or ::SDL_RELEASED */
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyButtonEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|the event type; SDL_JOYBUTTONDOWN or SDL_JOYBUTTONUP
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
|'''button'''
|the index of the button that changed
|-
|Uint8
|'''state'''
|the state of the button; SDL_PRESSED or SDL_RELEASED
|}

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_JoyAxisEvent](SDL_JoyAxisEvent)
[SDL_JoyBallEvent](SDL_JoyBallEvent)
[SDL_JoyHatEvent](SDL_JoyHatEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


