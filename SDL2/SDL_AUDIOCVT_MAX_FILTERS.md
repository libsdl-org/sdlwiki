###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AUDIOCVT_MAX_FILTERS

Upper limit of filters in [SDL_AudioCVT](SDL_AudioCVT)

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
#define SDL_AUDIOCVT_MAX_FILTERS 9
```

## Remarks

The maximum number of [SDL_AudioFilter](SDL_AudioFilter) functions in
[SDL_AudioCVT](SDL_AudioCVT) is currently limited to 9. The
[SDL_AudioCVT](SDL_AudioCVT).filters array has 10 pointers, one of which is
the terminating NULL pointer.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

