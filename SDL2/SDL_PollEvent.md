###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_PollEvent

Poll for currently pending events.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
int SDL_PollEvent(SDL_Event * event);

```

## Function Parameters

|               |                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------- |
| **event**     | the [SDL_Event](SDL_Event) structure to be filled with the next event from the queue, or NULL |

## Return Value

Returns 1 if there is a pending event or 0 if there are none available.

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

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetEventFilter](SDL_GetEventFilter)
* [SDL_PeepEvents](SDL_PeepEvents)
* [SDL_PushEvent](SDL_PushEvent)
* [SDL_SetEventFilter](SDL_SetEventFilter)
* [SDL_WaitEvent](SDL_WaitEvent)
* [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

