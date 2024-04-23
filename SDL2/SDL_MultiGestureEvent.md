###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_MultiGestureEvent

Multiple Finger Gesture Event (event.mgesture.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_MultiGestureEvent
{
    Uint32 type;        /**< ::SDL_MULTIGESTURE */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_TouchID touchId; /**< The touch device id */
    float dTheta;
    float dDist;
    float x;
    float y;
    Uint16 numFingers;
    Uint16 padding;
} SDL_MultiGestureEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_MULTIGESTURE
|-
|Uint32
|'''timestamp'''
|timestamp of the event
|-
|SDL_TouchID
|'''touchId'''
|the touch device id
|-
|float
|'''dTheta'''
|the amount that the fingers rotated during this motion, in radians
|-
|float
|'''dDist'''
|the amount that the fingers pinched during this motion
|-
|float
|'''x'''
|the normalized center of gesture
|-
|float
|'''y'''
|the normalized center of gesture
|-
|Uint16
|'''numFingers'''
|the number of fingers used in the gesture
|}

## Related Enumerations

:[[SDL_EventType]]

## Related Structures

:[[SDL_DollarGestureEvent]]
:[[SDL_Event]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)


