###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_HIDAPI_GAMECUBE_RUMBLE_BRAKE

A variable controlling whether rumble is used to implement the GameCube controller's 3 rumble modes, Stop(0), Rumble(1), and StopHard(2).

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_GAMECUBE_RUMBLE_BRAKE "SDL_JOYSTICK_HIDAPI_GAMECUBE_RUMBLE_BRAKE"
```

## Remarks

This is useful for applications that need full compatibility for things
like ADSR envelopes. - Stop is implemented by setting low_frequency_rumble
to 0 and high_frequency_rumble >0 - Rumble is both at any arbitrary value -
StopHard is implemented by setting both low_frequency_rumble and
high_frequency_rumble to 0

The variable can be set to the following values:

- "0": Normal rumble behavior is behavior is used. (default)
- "1": Proper GameCube controller rumble behavior is used.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

