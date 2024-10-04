###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_AUDIO_ALSA_DEFAULT_DEVICE

Specify the default ALSA audio device name.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_ALSA_DEFAULT_DEVICE "SDL_AUDIO_ALSA_DEFAULT_DEVICE"
```

## Remarks

This variable is a specific audio device to open when the "default" audio
device is used. By default if 4 channel audio is requested, the
"plug:surround40" device will be opened and if 6 channel audio is requested
the "plug:surround51" device will be opened.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

