# SDL_UpdateGamepads

Manually pump gamepad updates if not using the loop.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
void SDL_UpdateGamepads(void);
```

## Remarks

This function is called automatically by the event loop if events are
enabled. Under such circumstances, it will not be necessary to call this
function.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

