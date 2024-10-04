###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_AUDIO_FREQUENCY

A variable controlling the default audio frequency.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_FREQUENCY "SDL_AUDIO_FREQUENCY"
```

## Remarks

If the application doesn't specify the audio frequency when opening the
device, this hint can be used to specify a default frequency that will be
used. This defaults to "44100".

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

