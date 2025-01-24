# SDL_HINT_DIRECTINPUT_ENABLED

A variable that lets you disable the detection and use of DirectInput gamepad devices

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_DIRECTINPUT_ENABLED "SDL_DIRECTINPUT_ENABLED"
```

## Remarks

The variable can be set to the following values:

- "0": Disable DirectInput detection (only uses XInput)
- "1": Enable DirectInput detection (the default)





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

