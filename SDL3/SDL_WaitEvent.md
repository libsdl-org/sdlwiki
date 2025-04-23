# SDL_WaitEvent

Wait indefinitely for the next available event.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_WaitEvent(SDL_Event *event);
```

## Function Parameters

|                          |           |                                                                                                   |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------------- |
| [SDL_Event](SDL_Event) * | **event** | the [SDL_Event](SDL_Event) structure to be filled in with the next event from the queue, or NULL. |

## Return Value

(bool) Returns true on success or false if there was an error while waiting
for events; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that initialized the video
subsystem.

An application with no pending animations can conserve system resources and battery life by waiting for events between frames.
Then it is common practice to processes all events in a [SDL_PollEvent](SDL_PollEvent) loop before the next frame:

```c
while (app_is_running) {

    // draw and present the current frame

    SDL_WaitEvent(NULL);  // sleep until events are queued
    SDL_Event event;
    while (SDL_PollEvent(&event)) {  // poll until all events are handled
        // decide what to do with this event
    }
}
```

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_PushEvent](SDL_PushEvent)
- [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

