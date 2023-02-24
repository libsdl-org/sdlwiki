###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateGamepads

Manually pump gamepad updates if not using the loop.

## Syntax

```c
void SDL_UpdateGamepads(void);

```

## Remarks

This function is called automatically by the event loop if events are
enabled. Under such circumstances, it will not be necessary to call this
function.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

