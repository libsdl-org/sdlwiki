###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_ControllerAxisEvent

Game controller axis motion event structure (event.caxis.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_ControllerAxisEvent
{
    Uint32 type;        /**< ::SDL_CONTROLLERAXISMOTION */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_JoystickID which; /**< The joystick instance id */
    Uint8 axis;         /**< The controller axis (SDL_GameControllerAxis) */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;       /**< The axis value (range: -32768 to 32767) */
    Uint16 padding4;
} SDL_ControllerAxisEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_CONTROLLERAXISMOTION
|-
|Uint32
|'''timestamp'''
|the timestamp of the event
|-
|SDL_JoystickID
|'''which'''
|the joystick instance id
|-
|Uint8
|'''axis'''
|the controller axis ([SDL_GameControllerAxis](SDL_GameControllerAxis))
|-
|Sint16
|'''value'''
|the axis value (range: -32768 to 32767)
|}

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


