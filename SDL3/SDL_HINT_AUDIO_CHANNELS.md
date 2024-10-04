###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_AUDIO_CHANNELS

A variable controlling the default audio channel count.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_CHANNELS "SDL_AUDIO_CHANNELS"
```

## Remarks

If the application doesn't specify the audio channel count when opening the
device, this hint can be used to specify a default channel count that will
be used. This defaults to "1" for recording and "2" for playback devices.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

