###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadEventsEnabled

Query the state of gamepad event processing.

## Syntax

```c
SDL_bool SDL_GamepadEventsEnabled(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if gamepad events are being processed,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If gamepad events are disabled, you must call
[SDL_UpdateGamepads](SDL_UpdateGamepads)() yourself and check the state of
the gamepad when you want gamepad information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetGamepadEventsEnabled](SDL_SetGamepadEventsEnabled)

----
[CategoryAPI](CategoryAPI)

