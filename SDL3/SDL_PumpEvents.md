###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PumpEvents

Pump the event loop, gathering events from the input devices.

## Syntax

```c
void SDL_PumpEvents(void);

```

## Remarks

This function updates the event queue and internal input device state.

**WARNING**: This should only be run in the thread that initialized the
video subsystem, and for extra safety, you should consider only doing those
things on the main thread in any case.

[SDL_PumpEvents](SDL_PumpEvents.md)() gathers all the pending input
information from devices and places it in the event queue. Without calls to
[SDL_PumpEvents](SDL_PumpEvents.md)() no events would ever be placed on the
queue. Often the need for calls to [SDL_PumpEvents](SDL_PumpEvents.md)() is
hidden from the user since [SDL_PollEvent](SDL_PollEvent.md)() and
[SDL_WaitEvent](SDL_WaitEvent.md)() implicitly call
[SDL_PumpEvents](SDL_PumpEvents.md)(). However, if you are not polling or
waiting for events (e.g. you are filtering them), then you must call
[SDL_PumpEvents](SDL_PumpEvents.md)() to force an event queue update.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_PollEvent](SDL_PollEvent.md)
* [SDL_WaitEvent](SDL_WaitEvent.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryEvents](CategoryEvents.md)
