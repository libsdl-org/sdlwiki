###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_PushEvent

Add an event to the event queue.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
int SDL_PushEvent(SDL_Event * event);

```

## Function Parameters

|               |                                                     |
| ------------- | --------------------------------------------------- |
| **event**     | the [SDL_Event](SDL_Event) to be added to the queue |

## Return Value

Returns 1 on success, 0 if the event was filtered, or a negative error code
on failure; call [SDL_GetError](SDL_GetError)() for more information. A
common reason for error is the event queue being full.

## Remarks

The event queue can actually be used as a two way communication channel.
Not only can events be read from the queue, but the user can also push
their own events onto it. `event` is a pointer to the event structure you
wish to push onto the queue. The event is copied into the queue, and the
caller may dispose of the memory pointed to after
[SDL_PushEvent](SDL_PushEvent)() returns.

Note: Pushing device input events onto the queue doesn't modify the state
of the device within SDL.

This function is thread-safe, and can be called from other threads safely.

Note: Events pushed onto the queue with [SDL_PushEvent](SDL_PushEvent)()
get passed through the event filter but events added with
[SDL_PeepEvents](SDL_PeepEvents)() do not.

For pushing application-specific events, please use
[SDL_RegisterEvents](SDL_RegisterEvents)() to get an event type that does
not conflict with other code that also wants its own custom event types.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_PeepEvents](SDL_PeepEvents)
* [SDL_PollEvent](SDL_PollEvent)
* [SDL_RegisterEvents](SDL_RegisterEvents)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

