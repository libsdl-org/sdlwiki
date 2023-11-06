###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PollEvent

Poll for currently pending events.

## Syntax

```c
SDL_bool SDL_PollEvent(SDL_Event *event);

```

## Function Parameters

|               |                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------- |
| **event**     | the [SDL_Event](SDL_Event) structure to be filled with the next event from the queue, or NULL |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if this got an event or [SDL_FALSE](SDL_FALSE)
if there are none available.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`. The 1
returned refers to this event, immediately stored in the SDL Event
structure -- not an event to follow.

If `event` is NULL, it simply returns 1 if there is an event in the queue,
but will not remove it from the queue.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that set the video mode.

[SDL_PollEvent](SDL_PollEvent)() is the favored way of receiving system
events since it can be done from the main loop and does not suspend the
main loop while waiting on an event to be posted.

The common practice is to fully process the event queue once every frame,
usually as a first step before updating the game's state:

```c
while (game_is_still_running) {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {  // poll until all events are handled!
        // decide what to do with this event.
    }

    // update game state, draw the current frame
}
```

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PushEvent](SDL_PushEvent)
* [SDL_WaitEvent](SDL_WaitEvent)
* [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents)


