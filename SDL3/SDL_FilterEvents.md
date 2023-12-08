###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FilterEvents

Run a specific filter function on the current event queue, removing any events for which the filter returns 0.

## Syntax

```c
void SDL_FilterEvents(SDL_EventFilter filter, void *userdata);

```

## Function Parameters

|                  |                                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **filter**       | the [SDL_EventFilter](SDL_EventFilter.md) function to call when an event happens |
| **userdata**     | a pointer that is passed to `filter`                                          |

## Remarks

See [SDL_SetEventFilter](SDL_SetEventFilter.md)() for more information. Unlike
[SDL_SetEventFilter](SDL_SetEventFilter.md)(), this function does not change
the filter permanently, it only uses the supplied filter until this
function returns.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetEventFilter](SDL_GetEventFilter.md)
* [SDL_SetEventFilter](SDL_SetEventFilter.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryEvents](CategoryEvents.md)
