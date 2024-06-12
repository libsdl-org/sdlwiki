###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EventFilter

A function pointer used for callbacks that watch the event queue.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef int (SDLCALL *SDL_EventFilter)(void *userdata, SDL_Event *event);
```

## Function Parameters

|              |                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **userdata** | what was passed as `userdata` to [SDL_SetEventFilter](SDL_SetEventFilter)() or [SDL_AddEventWatch](SDL_AddEventWatch), etc |
| **event**    | the event that triggered the callback                                                                                      |

## Return Value

Returns 1 to permit event to be added to the queue, and 0 to disallow it.
When used with [SDL_AddEventWatch](SDL_AddEventWatch), the return value is
ignored.

## Thread Safety

SDL may call this callback at any time from any thread; the application is
responsible for locking resources the callback touches that need to be
protected.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_SetEventFilter](SDL_SetEventFilter)
- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryEvents](CategoryEvents)

