###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MouseRawAxisEvent

Mouse raw motion and wheel event structure (event.maxis.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_MouseRawAxisEvent
{
    SDL_EventType type; /**< SDL_EVENT_MOUSE_RAW_MOTION or SDL_EVENT_MOUSE_RAW_SCROLL */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_MouseID which;  /**< The mouse instance id, SDL_TOUCH_MOUSEID, or SDL_PEN_MOUSEID */
    int dx;             /**< The axis delta value in the X direction */
    int dy;             /**< The axis delta value in the Y direction */
    float ux;           /**< The denominator unit in the X direction */
    float uy;           /**< The denominator unit in the Y direction */
} SDL_MouseRawAxisEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

