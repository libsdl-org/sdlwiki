###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WaitEvent

Wait indefinitely for the next available event.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
int SDL_WaitEvent(SDL_Event * event);

```

## Function Parameters

|               |                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------ |
| **event**     | the [SDL_Event](SDL_Event) structure to be filled in with the next event from the queue, or NULL |

## Return Value

Returns 1 on success or 0 if there was an error while waiting for events;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that initialized the video
subsystem.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_PumpEvents](SDL_PumpEvents)
- [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

