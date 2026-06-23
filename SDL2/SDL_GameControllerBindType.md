# SDL_GameControllerBindType

Types of game controller control bindings.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
typedef enum SDL_GameControllerBindType
{
    SDL_CONTROLLER_BINDTYPE_NONE = 0,
    SDL_CONTROLLER_BINDTYPE_BUTTON,
    SDL_CONTROLLER_BINDTYPE_AXIS,
    SDL_CONTROLLER_BINDTYPE_HAT
} SDL_GameControllerBindType;
```

## Remarks

A game controller is a collection of bindings that map arbitrary joystick
buttons, axes and hat switches to specific positions on a generic
console-style gamepad.

## Version

This enum is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerButtonBind](SDL_GameControllerButtonBind)
- [SDL_GameControllerGetBindForAxis](SDL_GameControllerGetBindForAxis)
- [SDL_GameControllerGetBindForButton](SDL_GameControllerGetBindForButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGameController](CategoryGameController)

