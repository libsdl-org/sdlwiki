###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WaitEventTimeout

Wait until the specified timeout (in milliseconds) for the next available event.

## Syntax

```c
int SDL_WaitEventTimeout(SDL_Event * event,
                         int timeout);

```

## Function Parameters

|                 |                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------ |
| **event**       | the [SDL_Event](SDL_Event.md) structure to be filled in with the next event from the queue, or NULL |
| **timeout**     | the maximum number of milliseconds to wait for the next available event                          |

## Return Value

Returns 1 on success or 0 if there was an error while waiting for events;
call [SDL_GetError](SDL_GetError.md)() for more information. This also returns
0 if the timeout elapsed without an event arriving.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event.md) structure pointed to by `event`.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents.md)(),
you can only call this function in the thread that initialized the video
subsystem.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_PollEvent](SDL_PollEvent.md)
* [SDL_PumpEvents](SDL_PumpEvents.md)
* [SDL_WaitEvent](SDL_WaitEvent.md)

----
[CategoryAPI](CategoryAPI.md)
