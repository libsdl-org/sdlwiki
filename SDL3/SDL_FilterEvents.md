# SDL_FilterEvents

Run a specific filter function on the current event queue, removing any events for which the filter returns false.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_FilterEvents(SDL_EventFilter filter, void *userdata);
```

## Function Parameters

|                                    |              |                                                                                |
| ---------------------------------- | ------------ | ------------------------------------------------------------------------------ |
| [SDL_EventFilter](SDL_EventFilter) | **filter**   | the [SDL_EventFilter](SDL_EventFilter) function to call when an event happens. |
| void *                             | **userdata** | a pointer that is passed to `filter`.                                          |

## Remarks

See [SDL_SetEventFilter](SDL_SetEventFilter)() for more information. Unlike
[SDL_SetEventFilter](SDL_SetEventFilter)(), this function does not change
the filter permanently, it only uses the supplied filter until this
function returns.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetEventFilter](SDL_GetEventFilter)
- [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

