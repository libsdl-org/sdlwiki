###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetEventFilter

Query the current event filter.

## Syntax

```c
SDL_bool SDL_GetEventFilter(SDL_EventFilter *filter, void **userdata);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents)


