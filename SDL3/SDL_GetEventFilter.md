# SDL_GetEventFilter

Query the current event filter.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_GetEventFilter(SDL_EventFilter *filter, void **userdata);
```

## Function Parameters

|                                      |              |                                                                             |
| ------------------------------------ | ------------ | --------------------------------------------------------------------------- |
| [SDL_EventFilter](SDL_EventFilter) * | **filter**   | the current callback function will be stored here.                          |
| void **                              | **userdata** | the pointer that is passed to the current event filter will be stored here. |

## Return Value

(bool) Returns true on success or false if there is no event filter set.

## Remarks

This function can be used to "chain" filters, by saving the existing filter
before replacing it with a function that will call that saved filter.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

