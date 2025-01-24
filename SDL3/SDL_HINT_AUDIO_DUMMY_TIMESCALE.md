# SDL_HINT_AUDIO_DUMMY_TIMESCALE

A variable controlling the audio rate when using the dummy audio driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DUMMY_TIMESCALE "SDL_AUDIO_DUMMY_TIMESCALE"
```

## Remarks

The dummy audio driver normally simulates real-time for the audio rate that
was specified, but you can use this variable to adjust this rate higher or
lower down to 0. The default value is "1.0".

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

