###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_POLL_SENTINEL

A variable controlling the use of a sentinel event when polling the event queue

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_POLL_SENTINEL "SDL_POLL_SENTINEL"
```

## Remarks

This variable can be set to the following values:

- "0": Disable poll sentinels
- "1": Enable poll sentinels

When polling for events, [SDL_PumpEvents](SDL_PumpEvents) is used to gather
new events from devices. If a device keeps producing new events between
calls to [SDL_PumpEvents](SDL_PumpEvents), a poll loop will become stuck
until the new events stop. This is most noticeable when moving a high
frequency mouse.

By default, poll sentinels are enabled.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

