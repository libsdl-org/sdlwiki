###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PenAxisEvent

Pressure-sensitive pen pressure / angle event structure (event.paxis.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PenAxisEvent
{
    SDL_EventType type;     /**< SDL_EVENT_PEN_AXIS */
    Uint32 reserved;
    Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;  /**< The window with pen focus, if any */
    SDL_PenID which;        /**< The pen instance id */
    SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
    float x;                /**< X coordinate, relative to window */
    float y;                /**< Y coordinate, relative to window */
    SDL_PenAxis axis;       /**< Axis that has changed */
    float value;            /**< New value of axis */
} SDL_PenAxisEvent;
```

## Remarks

You might get some of these events even if the pen isn't touching the
tablet.

## Version

This struct is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryPen](CategoryPen)


