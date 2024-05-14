###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUDIO_DEVICE_STREAM_NAME

Specify an application name for an audio device.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_STREAM_NAME "SDL_AUDIO_DEVICE_STREAM_NAME"
```

## Remarks

Some audio backends (such as PulseAudio) allow you to describe your audio
stream. Among other things, this description might show up in a system
control panel that lets the user adjust the volume on specific audio
streams instead of using one giant master volume slider.

This hints lets you transmit that information to the OS. The contents of
this hint are used while opening an audio device. You should use a string
that describes your what your program is playing ("audio stream" is
probably sufficient in many cases, but this could be useful for something
like "team chat" if you have a headset playing VoIP audio separately).

Setting this to "" or leaving it unset will have SDL use a reasonable
default: "audio stream" or something similar.

On targets where this is not supported, this hint does nothing.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

