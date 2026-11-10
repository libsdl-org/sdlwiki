# SDL_HINT_JOYSTICK_ASYNC

A variable controlling whether a separate thread should be used for joystick detection and updates.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ASYNC "SDL_JOYSTICK_ASYNC"
```

## Remarks

If this is enabled, joystick initialization will return immediately.
Connected joysticks and gamepads will not be immediately visible, they will
come in as hotplug events in the background.
[SDL_UpdateJoysticks](SDL_UpdateJoysticks)() will also return immediately
and joystick state will be updated asynchronously in the background.
Joystick and gamepad events are delivered off the main thread.

If you enable this hint, you should not hold the joystick lock while
quitting the joystick subsystem.

The variable can be set to the following values:

- "0": A separate thread is not used. (default)
- "1": A separate thread is used for joystick updates.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

