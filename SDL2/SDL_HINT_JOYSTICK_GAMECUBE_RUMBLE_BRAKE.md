###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_GAMECUBE_RUMBLE_BRAKE

A variable controlling whether "low_frequency_rumble" and "high_frequency_rumble" is used to implement the GameCube controller's 3 rumble modes, Stop(0), Rumble(1), and StopHard(2) this is useful for applications that need full compatibility for things like ADSR envelopes.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_GAMECUBE_RUMBLE_BRAKE "SDL_JOYSTICK_GAMECUBE_RUMBLE_BRAKE"
```

## Remarks

Stop is implemented by setting "low_frequency_rumble" to "0" and
"high_frequency_rumble" ">0" Rumble is both at any arbitrary value,
StopHard is implemented by setting both "low_frequency_rumble" and
"high_frequency_rumble" to "0"

This variable can be set to the following values:

- "0": Normal rumble behavior is behavior is used (default)
- "1": Proper GameCube controller rumble behavior is used

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

