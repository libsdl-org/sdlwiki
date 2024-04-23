###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_JoyDeviceEvent

Joystick device event structure (event.jdevice.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_JoyDeviceEvent
{
    Uint32 type;        /**< ::SDL_JOYDEVICEADDED or ::SDL_JOYDEVICEREMOVED */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Sint32 which;       /**< The joystick device index for the ADDED event, instance id for the REMOVED event */
} SDL_JoyDeviceEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_JOYDEVICEADDED or SDL_JOYDEVICEREMOVED
|-
|Uint32
|'''timestamp'''
|the timestamp of the event
|-
|Sint32
|'''which'''
|the joystick device index for the SDL_JOYDEVICEADDED event or the instance id for the SDL_JOYDEVICEREMOVED event
|}

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


