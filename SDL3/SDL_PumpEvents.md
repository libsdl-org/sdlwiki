###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PumpEvents

Pump the event loop, gathering events from the input devices.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_PumpEvents(void);
```

## Remarks

This function updates the event queue and internal input device state.

[SDL_PumpEvents](SDL_PumpEvents)() gathers all the pending input
information from devices and places it in the event queue. Without calls to
[SDL_PumpEvents](SDL_PumpEvents)() no events would ever be placed on the
queue. Often the need for calls to [SDL_PumpEvents](SDL_PumpEvents)() is
hidden from the user since [SDL_PollEvent](SDL_PollEvent)() and
[SDL_WaitEvent](SDL_WaitEvent)() implicitly call
[SDL_PumpEvents](SDL_PumpEvents)(). However, if you are not polling or
waiting for events (e.g. you are filtering them), then you must call
[SDL_PumpEvents](SDL_PumpEvents)() to force an event queue update.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PollEvent](SDL_PollEvent)
- [SDL_WaitEvent](SDL_WaitEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

