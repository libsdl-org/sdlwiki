# SDL_SetGamepadEventsEnabled

Set the state of gamepad event processing.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
void SDL_SetGamepadEventsEnabled(bool enabled);
```

## Function Parameters

|      |             |                                           |
| ---- | ----------- | ----------------------------------------- |
| bool | **enabled** | whether to process gamepad events or not. |

## Remarks

If gamepad events are disabled, you must call
[SDL_UpdateGamepads](SDL_UpdateGamepads)() yourself and check the state of
the gamepad when you want gamepad information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GamepadEventsEnabled](SDL_GamepadEventsEnabled)
- [SDL_UpdateGamepads](SDL_UpdateGamepads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

