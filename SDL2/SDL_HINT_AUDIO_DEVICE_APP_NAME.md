###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUDIO_DEVICE_APP_NAME

Specify an application name for an audio device.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_APP_NAME "SDL_AUDIO_DEVICE_APP_NAME"
```

## Remarks

Some audio backends (such as PulseAudio) allow you to describe your audio
stream. Among other things, this description might show up in a system
control panel that lets the user adjust the volume on specific audio
streams instead of using one giant master volume slider.

This hints lets you transmit that information to the OS. The contents of
this hint are used while opening an audio device. You should use a string
that describes your program ("My Game 2: The Revenge")

Setting this to "" or leaving it unset will have SDL use a reasonable
default: this will be the name set with
[SDL_HINT_APP_NAME](SDL_HINT_APP_NAME), if that hint is set. Otherwise,
it'll probably the application's name or "SDL Application" if SDL doesn't
have any better information.

On targets where this is not supported, this hint does nothing.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

