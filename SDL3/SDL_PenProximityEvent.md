# SDL_PenProximityEvent

Pressure-sensitive pen proximity event structure (event.pproximity.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_PenProximityEvent
{
    SDL_EventType type; /**< SDL_EVENT_PEN_PROXIMITY_IN or SDL_EVENT_PEN_PROXIMITY_OUT */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with pen focus, if any */
    SDL_PenID which;        /**< The pen instance id */
} SDL_PenProximityEvent;
```

## Remarks

When a pen becomes visible to the system (it is close enough to a tablet,
etc), SDL will send an
[SDL_EVENT_PEN_PROXIMITY_IN](SDL_EVENT_PEN_PROXIMITY_IN) event with the new
pen's ID. This ID is valid until the pen leaves proximity again (has been
removed from the tablet's area, the tablet has been unplugged, etc). If the
same pen reenters proximity again, it will be given a new ID.

Note that "proximity" means "close enough for the tablet to know the tool
is there." The pen touching and lifting off from the tablet while not
leaving the area are handled by [SDL_EVENT_PEN_DOWN](SDL_EVENT_PEN_DOWN)
and [SDL_EVENT_PEN_UP](SDL_EVENT_PEN_UP).

Not all platforms have a window associated with the pen during proximity
events. Some wait until motion/button/etc events to offer this info.

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryPen](CategoryPen)


