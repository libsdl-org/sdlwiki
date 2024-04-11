###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUDIO_INCLUDE_MONITORS

A variable that causes SDL to not ignore audio "monitors"

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_AUDIO_INCLUDE_MONITORS "SDL_AUDIO_INCLUDE_MONITORS"
```

## Remarks

This is currently only used for PulseAudio and ignored elsewhere.

By default, SDL ignores audio devices that aren't associated with physical
hardware. Changing this hint to "1" will expose anything SDL sees that
appears to be an audio source or sink. This will add "devices" to the list
that the user probably doesn't want or need, but it can be useful in
scenarios where you want to hook up SDL to some sort of virtual device,
etc.

The default value is "0". This hint must be set before
[SDL_Init](SDL_Init)().

This hint is available since SDL 2.0.16. Before then, virtual devices are
always ignored.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

