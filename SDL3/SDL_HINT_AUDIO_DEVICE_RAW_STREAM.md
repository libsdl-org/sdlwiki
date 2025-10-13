# SDL_HINT_AUDIO_DEVICE_RAW_STREAM

Specify whether this audio device should do audio processing.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_RAW_STREAM "SDL_AUDIO_DEVICE_RAW_STREAM"
```

## Remarks

Some operating systems perform echo cancellation, gain control, and noise
reduction as needed. If your application already handles these, you can set
this hint to prevent the OS from doing additional audio processing.

This corresponds to the WASAPI audio option `AUDCLNT_STREAMOPTIONS_RAW`.

The variable can be set to the following values:

- "0": audio processing can be done by the OS. (default)
- "1": audio processing is done by the application.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

