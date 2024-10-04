###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetEventFilter](SDL_SetEventFilter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

