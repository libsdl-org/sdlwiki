###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_AUDIO_DEVICE_SAMPLE_FRAMES

A variable controlling device buffer size.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_SAMPLE_FRAMES "SDL_AUDIO_DEVICE_SAMPLE_FRAMES"
```

## Remarks

This hint is an integer > 0, that represents the size of the device's
buffer in sample frames (stereo audio data in 16-bit format is 4 bytes per
sample frame, for example).

SDL3 generally decides this value on behalf of the app, but if for some
reason the app needs to dictate this (because they want either lower
latency or higher throughput AND ARE WILLING TO DEAL WITH what that might
require of the app), they can specify it.

SDL will try to accommodate this value, but there is no promise you'll get
the buffer size requested. Many platforms won't honor this request at all,
or might adjust it.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

