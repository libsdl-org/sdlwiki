###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_AUDIO_CATEGORY

A variable controlling the audio category on iOS and macOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_CATEGORY   "SDL_AUDIO_CATEGORY"
```

## Remarks

The variable can be set to the following values:

- "ambient": Use the AVAudioSessionCategoryAmbient audio category, will be
  muted by the phone mute switch (default)
- "playback": Use the AVAudioSessionCategoryPlayback category.

For more information, see Apple's documentation:
https://developer.apple.com/library/content/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioSessionCategoriesandModes/AudioSessionCategoriesandModes.html

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

