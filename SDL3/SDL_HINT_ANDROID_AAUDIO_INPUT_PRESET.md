# SDL_HINT_ANDROID_AAUDIO_INPUT_PRESET

A variable to control Android's AAudio input preset.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_AAUDIO_INPUT_PRESET "SDL_ANDROID_AAUDIO_INPUT_PRESET"
```

## Remarks

This hint only applies to SDL's "aaudio" backend on Android 9+ devices.

Some devices choose the wrong microphone by default (between the one meant
to be spoken in when the phone is held to the user's ear for a phone call,
or an external microphone that's meant to be used when recording video), or
have DSP effects applied to the recorded audio, and changing the input
preset can help control this.

This can be any number that maps to an `AAUDIO_INPUT_PRESET_*` enum from
the Android NDK headers. The most reasonable choices are 5 ("camcorder",
for external microphones) and 7 ("voice communication", for speaking
directly into the device like a mobile phone). 6 ("voice recognition")
might also be a useful choice.

If unset (the default), SDL will not specify an input preset at all, which
lets the system choose. This is usually the correct thing to do unless your
app is having problems.

This hint should be set before a recording audio device is opened.

## Version

This hint is available since SDL 3.4.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

