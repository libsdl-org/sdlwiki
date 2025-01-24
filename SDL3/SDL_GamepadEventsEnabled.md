# SDL_GamepadEventsEnabled

Query the state of gamepad event processing.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GamepadEventsEnabled(void);
```

## Return Value

(bool) Returns true if gamepad events are being processed, false otherwise.

## Remarks

If gamepad events are disabled, you must call
[SDL_UpdateGamepads](SDL_UpdateGamepads)() yourself and check the state of
the gamepad when you want gamepad information.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetGamepadEventsEnabled](SDL_SetGamepadEventsEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

