# SDL_PenMotionEvent

Pressure-sensitive pen motion event structure (event.pmotion.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PenMotionEvent
{
    SDL_EventType type; /**< SDL_EVENT_PEN_MOTION */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with pen focus, if any */
    SDL_PenID which;        /**< The pen instance id */
    SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
    float x;                /**< X coordinate, relative to window */
    float y;                /**< Y coordinate, relative to window */
} SDL_PenMotionEvent;
```

## Remarks

Depending on the hardware, you may get motion events when the pen is not
touching a tablet, for tracking a pen even when it isn't drawing. You
should listen for [SDL_EVENT_PEN_DOWN](SDL_EVENT_PEN_DOWN) and
[SDL_EVENT_PEN_UP](SDL_EVENT_PEN_UP) events, or check `pen_state &
SDL_PEN_INPUT_DOWN` to decide if a pen is "drawing" when dealing with pen
motion.

## Version

This struct is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryPen](CategoryPen)


