###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SysWMEvent

A video driver dependent system event (event.syswm.*) This event is disabled by default, you can enable it with [SDL_EventState](SDL_EventState)()

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_SysWMEvent
{
    Uint32 type;        /**< ::SDL_SYSWMEVENT */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    SDL_SysWMmsg *msg;  /**< driver dependent data, defined in SDL_syswm.h */
} SDL_SysWMEvent;
```

## Data Fields

|                               |                 |                                               |
| ----------------------------- | --------------- | --------------------------------------------- |
| Uint32                        | '''type'''      | SDL_SYSWMEVENT                                |
| Uint32                        | '''timestamp''' | timestamp of the event                        |
| [SDL_SysWMmsg](SDL_SysWMmsg)* | '''msg'''       | driver dependent data, defined in SDL_syswm.h |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)
[SDL_SysWMinfo](SDL_SysWMinfo)
[SDL_SysWMmsg](SDL_SysWMmsg)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


