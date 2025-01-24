# SDL_HINT_ANDROID_LOW_LATENCY_AUDIO

A variable to control whether low latency audio should be enabled.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_LOW_LATENCY_AUDIO "SDL_ANDROID_LOW_LATENCY_AUDIO"
```

## Remarks

Some devices have poor quality output when this is enabled, but this is
usually an improvement in audio latency.

The variable can be set to the following values:

- "0": Low latency audio is not enabled.
- "1": Low latency audio is enabled. (default)

This hint should be set before SDL audio is initialized.

## Version

This hint is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

