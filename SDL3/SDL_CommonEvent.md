# SDL_CommonEvent

Fields shared by every event (event.common.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_CommonEvent
{
    Uint32 type;        /**< Event type, shared with all events, Uint32 to cover user events which are not in the SDL_EventType enumeration */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
} SDL_CommonEvent;
```

## Remarks

All the individual structs that comprise the [SDL_Event](SDL_Event) union
start with these same fields, so you can access them from any struct
directly.

Event types that don't have further data in a specific struct will still
have valid CommonEvent data, accessible via the event.common field.

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

