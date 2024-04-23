###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUDIO_RESAMPLING_MODE

A variable controlling speed/quality tradeoff of audio resampling.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_RESAMPLING_MODE   "SDL_AUDIO_RESAMPLING_MODE"
```

## Remarks

If available, SDL can use libsamplerate ( http://www.mega-nerd.com/SRC/ )
to handle audio resampling. There are different resampling modes available
that produce different levels of quality, using more CPU.

If this hint isn't specified to a valid setting, or libsamplerate isn't
available, SDL will use the default, internal resampling algorithm.

As of SDL 2.26, [SDL_ConvertAudio](SDL_ConvertAudio)() respects this hint
when libsamplerate is available.

This hint is currently only checked at audio subsystem initialization.

This variable can be set to the following values:

- "0" or "default": Use SDL's internal resampling (Default when not set -
  low quality, fast)
- "1" or "fast": Use fast, slightly higher quality resampling, if available
- "2" or "medium": Use medium quality resampling, if available
- "3" or "best": Use high quality resampling, if available

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

