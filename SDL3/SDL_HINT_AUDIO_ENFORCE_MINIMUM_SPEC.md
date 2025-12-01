# SDL_HINT_AUDIO_ENFORCE_MINIMUM_SPEC

A variable controlling whether SDL enforces a minimum audio device spec.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_ENFORCE_MINIMUM_SPEC "SDL_AUDIO_ENFORCE_MINIMUM_SPEC"
```

## Remarks

By default, SDL will require devices to be opened at a minimum spec (at
time of writing: 44100Hz, stereo, [Sint16](Sint16) format), so if something
lower quality tries to open the device first, it doesn't ruin audio for the
next thing that opens a device. For example, if a VoIP library wants Uint8,
8000Hz, mono output, it doesn't force the entire game to this state simply
because it got there first.

However, an app that knows it will definitely be the only thing opening a
device, and wants to open it at a lower spec, might be able to avoid some
otherwise-unnecessary conversions by bypassing this minimum requirement.

Note that even without the minimum enforcement, the system might choose a
different format/channels/frequency than requested by the app; this hint
just removes SDL's minimum policy.

The variable can be set to the following values:

- "0": Audio device mimimum formats _are not_ enforced.
- "1": Audio device minimum formats _are_ enforced. (default)

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

