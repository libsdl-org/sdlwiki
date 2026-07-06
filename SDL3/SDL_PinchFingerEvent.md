# SDL_PinchFingerEvent

Pinch event structure (event.pinch.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PinchFingerEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_PINCH_BEGIN or ::SDL_EVENT_PINCH_UPDATE or ::SDL_EVENT_PINCH_END */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    float scale;        /**< The scale change since the last SDL_EVENT_PINCH_UPDATE. Scale < 1 is "zoom out". Scale > 1 is "zoom in". */
    SDL_WindowID windowID; /**< The window underneath the finger, if any */
    float span_x;        /**< On mobile devices for BEGIN and UPDATE events, the average X distance between each of the pointers forming the pinch in window coordinates.  Otherwise, -1. */
    float span_y;        /**< On mobile devices for BEGIN and UPDATE events, the average Y distance between each of the pointers forming the pinch in window coordinates.  Otherwise, -1. */
    float focus_x;        /**< On mobile devices for BEGIN and UPDATE events, the X coordinate of the current gesture's focal point in window coordinates.  Otherwise, -1. */
    float focus_y;        /**< On mobile devices for BEGIN and UPDATE events, the Y coordinate of the current gesture's focal point in window coordinates.  Otherwise, -1. */
} SDL_PinchFingerEvent;
```

## Remarks

span_(x/y) and focus_(x/y) are only available for pinch gestures on mobile
devices

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

