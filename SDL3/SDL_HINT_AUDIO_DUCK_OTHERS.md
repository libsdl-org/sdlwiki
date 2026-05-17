# SDL_HINT_AUDIO_DUCK_OTHERS

Specify whether this audio stream should duck other audio.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DUCK_OTHERS "SDL_AUDIO_DUCK_OTHERS"
```

## Remarks

On Apple platforms, this hint controls whether other audio streams are
ducked (reduced in volume) while your application is in the foreground.

The variable can be set to the following values:

- "0": Other audio will not be ducked. (default)
- "1": Other audio will be ducked.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

