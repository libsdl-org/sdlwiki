# SDL_GamepadBindingType

Types of gamepad control bindings.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
typedef enum SDL_GamepadBindingType
{
    SDL_GAMEPAD_BINDTYPE_NONE = 0,
    SDL_GAMEPAD_BINDTYPE_BUTTON,
    SDL_GAMEPAD_BINDTYPE_AXIS,
    SDL_GAMEPAD_BINDTYPE_HAT
} SDL_GamepadBindingType;
```

## Remarks

A gamepad is a collection of bindings that map arbitrary joystick buttons,
axes and hat switches to specific positions on a generic console-style
gamepad. This enum is used as part of
[SDL_GamepadBinding](SDL_GamepadBinding) to specify those mappings.

## Version

This enum is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGamepad](CategoryGamepad)

