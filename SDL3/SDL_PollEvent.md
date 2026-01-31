# SDL_PollEvent

Poll for currently pending events.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_PollEvent(SDL_Event *event);
```

## Function Parameters

|                          |           |                                                                                                |
| ------------------------ | --------- | ---------------------------------------------------------------------------------------------- |
| [SDL_Event](SDL_Event) * | **event** | the [SDL_Event](SDL_Event) structure to be filled with the next event from the queue, or NULL. |

## Return Value

(bool) Returns true if this got an event or false if there are none
available.

## Remarks

If `event` is not NULL, the next event is removed from the queue and stored
in the [SDL_Event](SDL_Event) structure pointed to by `event`.

If `event` is NULL, it simply returns true if there is an event in the
queue, but will not remove it from the queue.

As this function may implicitly call [SDL_PumpEvents](SDL_PumpEvents)(),
you can only call this function in the thread that initialized the video
subsystem.

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

Note that Windows (and possibly other platforms) has a quirk about how it
handles events while dragging/resizing a window, which can cause this
function to block for significant amounts of time. Technical explanations
and solutions are discussed on the wiki:

https://wiki.libsdl.org/SDL3/AppFreezeDuringDrag

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PushEvent](SDL_PushEvent)
- [SDL_WaitEvent](SDL_WaitEvent)
- [SDL_WaitEventTimeout](SDL_WaitEventTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

