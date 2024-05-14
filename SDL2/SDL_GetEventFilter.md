###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetEventFilter

Query the current event filter.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
SDL_bool SDL_GetEventFilter(SDL_EventFilter * filter,
                            void **userdata);

```

## Function Parameters

|                  |                                                                            |
| ---------------- | -------------------------------------------------------------------------- |
| **filter**       | the current callback function will be stored here                          |
| **userdata**     | the pointer that is passed to the current event filter will be stored here |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) on success or [SDL_FALSE](SDL_FALSE) if there
is no event filter set.

## Remarks

This function can be used to "chain" filters, by saving the existing filter
before replacing it with a function that will call that saved filter.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

