###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenMotionEvent

Pressure-sensitive pen motion / pressure / angle event structure (event.pmotion.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PenMotionEvent
{
    SDL_EventType type;     /**< SDL_EVENT_PEN_MOTION */
    Uint32 reserved;
    Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;  /**< The window with pen focus, if any */
    SDL_PenID which;        /**< The pen instance id */
    Uint8 padding1;
    Uint8 padding2;
    Uint16 pen_state;       /**< Pen button masks (where SDL_BUTTON(1) is the first button, SDL_BUTTON(2) is the second button etc.), SDL_PEN_DOWN_MASK is set if the pen is touching the surface, and SDL_PEN_ERASER_MASK is set if the pen is (used as) an eraser. */
    float x;                /**< X coordinate, relative to window */
    float y;                /**< Y coordinate, relative to window */
    float axes[SDL_PEN_NUM_AXES];   /**< Pen axes such as pressure and tilt (ordered as per SDL_PenAxis) */
} SDL_PenMotionEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

