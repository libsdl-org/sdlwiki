###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_EventState

Set the state of processing events by type.

## Syntax

```c
Uint8 SDL_EventState(Uint32 type, int state);

```

## Function Parameters

|               |                                                                   |
| ------------- | ----------------------------------------------------------------- |
| **type**      | the type of event; see [SDL_EventType](SDL_EventType) for details |
| **state**     | how to process the event                                          |

## Return Value

Returns `[SDL_DISABLE](SDL_DISABLE)` or `[SDL_ENABLE](SDL_ENABLE)`,
representing the processing state of the event before this function makes
any changes to it.

## Remarks

`state` may be any of the following:

- `[SDL_QUERY](SDL_QUERY)`: returns the current processing state of the
  specified event
- `[SDL_IGNORE](SDL_IGNORE)` (aka `[SDL_DISABLE](SDL_DISABLE)`): the event
  will automatically be dropped from the event queue and will not be
  filtered
- `[SDL_ENABLE](SDL_ENABLE)`: the event will be processed normally

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetEventState](SDL_GetEventState)

----
[CategoryAPI](CategoryAPI)

