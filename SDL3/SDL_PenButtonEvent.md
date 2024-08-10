###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenButtonEvent

Pressure-sensitive pen button event structure (event.pbutton.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PenButtonEvent
{
    SDL_EventType type; /**< SDL_EVENT_PEN_BUTTON_DOWN or SDL_EVENT_PEN_BUTTON_UP */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with mouse focus, if any */
    SDL_PenID which;        /**< The pen instance id */
    SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
    float x;                /**< X position of pen on tablet */
    float y;                /**< Y position of pen on tablet */
    Uint8 button;       /**< The pen button index (first button is 1). */
    Uint8 state;        /**< SDL_PRESSED or SDL_RELEASED */
} SDL_PenButtonEvent;
```

## Remarks

This is for buttons on the pen itself that the user might click. The pen
itself pressing down to draw triggers a
[SDL_EVENT_PEN_DOWN](SDL_EVENT_PEN_DOWN) event instead.

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

