# SDL_HINT_AUDIO_FORMAT

A variable controlling the default audio format.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_FORMAT "SDL_AUDIO_FORMAT"
```

## Remarks

If the application doesn't specify the audio format when opening the
device, this hint can be used to specify a default format that will be
used.

The variable can be set to the following values:

- "U8": Unsigned 8-bit audio
- "S8": Signed 8-bit audio
- "S16LE": Signed 16-bit little-endian audio
- "S16BE": Signed 16-bit big-endian audio
- "S16": Signed 16-bit native-endian audio (default)
- "S32LE": Signed 32-bit little-endian audio
- "S32BE": Signed 32-bit big-endian audio
- "S32": Signed 32-bit native-endian audio
- "F32LE": Floating point little-endian audio
- "F32BE": Floating point big-endian audio
- "F32": Floating point native-endian audio

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

