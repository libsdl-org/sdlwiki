###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_AUDIO_INCLUDE_MONITORS

A variable that causes SDL to not ignore audio "monitors".

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_INCLUDE_MONITORS "SDL_AUDIO_INCLUDE_MONITORS"
```

## Remarks

This is currently only used by the PulseAudio driver.

By default, SDL ignores audio devices that aren't associated with physical
hardware. Changing this hint to "1" will expose anything SDL sees that
appears to be an audio source or sink. This will add "devices" to the list
that the user probably doesn't want or need, but it can be useful in
scenarios where you want to hook up SDL to some sort of virtual device,
etc.

The variable can be set to the following values:

- "0": Audio monitor devices will be ignored. (default)
- "1": Audio monitor devices will show up in the device list.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

