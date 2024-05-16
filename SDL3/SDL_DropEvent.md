###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DropEvent

An event used to drop text or request a file open by the system (event.drop.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_DropEvent
{
    SDL_EventType type; /**< SDL_EVENT_DROP_BEGIN or SDL_EVENT_DROP_FILE or SDL_EVENT_DROP_TEXT or SDL_EVENT_DROP_COMPLETE or SDL_EVENT_DROP_POSITION */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;    /**< The window that was dropped on, if any */
    float x;            /**< X coordinate, relative to window (not on begin) */
    float y;            /**< Y coordinate, relative to window (not on begin) */
    char *source;       /**< The source app that sent this drop event, or NULL if that isn't available */
    char *data;         /**< The text for SDL_EVENT_DROP_TEXT and the file name for SDL_EVENT_DROP_FILE, NULL for other events */
} SDL_DropEvent;
```

## Remarks

The `data` is owned by SDL and should be copied if the application wants to
hold onto it beyond the scope of handling this event. Do not free it!

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

