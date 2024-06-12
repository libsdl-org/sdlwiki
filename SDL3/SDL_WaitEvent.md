###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitEvent

Wait indefinitely for the next available event.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
SDL_bool SDL_WaitEvent(SDL_Event *event);
```

## Function Parameters

|                          |           |                                                                                                  |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------------ |
| [SDL_Event](SDL_Event) * | **event** | the [SDL_Event](SDL_Event) structure to be filled in with the next event from the queue, or NULL |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) if there was an error while waiting for events; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that initialized the video
subsystem.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_PushEvent](SDL_PushEvent)
- [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

