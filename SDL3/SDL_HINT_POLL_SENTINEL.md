###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_POLL_SENTINEL

A variable controlling the use of a sentinel event when polling the event queue.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_POLL_SENTINEL "SDL_POLL_SENTINEL"
```

## Remarks

When polling for events, [SDL_PumpEvents](SDL_PumpEvents) is used to gather
new events from devices. If a device keeps producing new events between
calls to [SDL_PumpEvents](SDL_PumpEvents), a poll loop will become stuck
until the new events stop. This is most noticeable when moving a high
frequency mouse.

The variable can be set to the following values:

- "0": Disable poll sentinels.
- "1": Enable poll sentinels. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

