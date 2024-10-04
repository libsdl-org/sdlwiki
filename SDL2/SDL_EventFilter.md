###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_EventFilter

A function pointer used for callbacks that watch the event queue.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef int (SDLCALL * SDL_EventFilter) (void *userdata, SDL_Event * event);
```

## Function Parameters

|              |                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **userdata** | what was passed as `userdata` to [SDL_SetEventFilter](SDL_SetEventFilter)() or [SDL_AddEventWatch](SDL_AddEventWatch), etc. |
| **event**    | the event that triggered the callback.                                                                                      |

## Return Value

Returns 1 to permit event to be added to the queue, and 0 to disallow it.
When used with [SDL_AddEventWatch](SDL_AddEventWatch), the return value is
ignored.

## See Also

- [SDL_SetEventFilter](SDL_SetEventFilter)
- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryEvents](CategoryEvents)

