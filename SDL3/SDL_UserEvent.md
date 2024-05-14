###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UserEvent

A user-defined event type (event.user.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_UserEvent
{
    Uint32 type;        /**< ::SDL_EVENT_USER through ::SDL_EVENT_LAST-1, Uint32 because these are not in the SDL_EventType enumeration */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The associated window if any */
    Sint32 code;        /**< User defined event code */
    void *data1;        /**< User defined data pointer */
    void *data2;        /**< User defined data pointer */
} SDL_UserEvent;
```

## Remarks

This event is unique; it is never created by SDL, but only by the
application. The event can be pushed onto the event queue using
[SDL_PushEvent](SDL_PushEvent)(). The contents of the structure members are
completely up to the programmer; the only requirement is that '''type''' is
a value obtained from [SDL_RegisterEvents](SDL_RegisterEvents)().

## Version

This struct is available since SDL 3.0.0.

## Code Examples

```c
extern Sint32 my_event_code;
extern void *significant_data;
extern void *some_other_data;

const Uint32 myEventType = SDL_RegisterEvents(1);
if (myEventType != ((Uint32)-1)) {
    SDL_Event event;
    SDL_zero(event);
    event.type = myEventType;
    event.user.code = my_event_code;
    event.user.data1 = significant_data;
    event.user.data2 = some_other_data;
    SDL_PushEvent(&event);
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

