###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_AUDIO_DISK_TIMESCALE

A variable controlling the audio rate when using the disk audio driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DISK_TIMESCALE "SDL_AUDIO_DISK_TIMESCALE"
```

## Remarks

The disk audio driver normally simulates real-time for the audio rate that
was specified, but you can use this variable to adjust this rate higher or
lower down to 0. The default value is "1.0".

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

