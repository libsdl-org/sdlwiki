###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowEvent

Window state change event data (event.window.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_WindowEvent
{
    SDL_EventType type; /**< SDL_EVENT_WINDOW_* */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The associated window */
    Sint32 data1;       /**< event dependent data */
    Sint32 data2;       /**< event dependent data */
} SDL_WindowEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

