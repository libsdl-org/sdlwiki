# SDL_HINT_JOYSTICK_ASYNC_UPDATE_INTERVAL

A variable controlling the polling interval for asynchronous joystick updates.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ASYNC_UPDATE_INTERVAL "SDL_JOYSTICK_ASYNC_UPDATE_INTERVAL"
```

## Remarks

If this hint is set to "-1" (the default), asynchronous joystick updates
will be triggered when the event loop runs. Otherwise this value is the
polling interval, in milliseconds, for asynchronous joystick updates.

Regardless of the value of this hint, you can trigger an update at a
specific time using [SDL_UpdateJoysticks](SDL_UpdateJoysticks)()

This hint can be set anytime.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

