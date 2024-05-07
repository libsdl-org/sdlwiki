###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FilterEvents

Run a specific filter function on the current event queue, removing any events for which the filter returns 0.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
void SDL_FilterEvents(SDL_EventFilter filter,
                      void *userdata);

```

## Function Parameters

|                  |                                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **filter**       | the [SDL_EventFilter](SDL_EventFilter) function to call when an event happens |
| **userdata**     | a pointer that is passed to `filter`                                          |

## Remarks

See [SDL_SetEventFilter](SDL_SetEventFilter)() for more information. Unlike
[SDL_SetEventFilter](SDL_SetEventFilter)(), this function does not change
the filter permanently, it only uses the supplied filter until this
function returns.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetEventFilter](SDL_GetEventFilter)
- [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

