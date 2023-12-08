###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerUpdate

Manually pump game controller updates if not using the loop.

## Syntax

```c
void SDL_GameControllerUpdate(void);

```

## Remarks

This function is called automatically by the event loop if events are
enabled. Under such circumstances, it will not be necessary to call this
function.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
