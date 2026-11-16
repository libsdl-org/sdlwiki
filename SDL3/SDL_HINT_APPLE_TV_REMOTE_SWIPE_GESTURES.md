# SDL_HINT_APPLE_TV_REMOTE_SWIPE_GESTURES

A variable controlling whether the Apple TV remote's touchpad swipe gesture recognizers are installed.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APPLE_TV_REMOTE_SWIPE_GESTURES "SDL_APPLE_TV_REMOTE_SWIPE_GESTURES"
```

## Remarks

On tvOS SDL installs UISwipeGestureRecognizers so that swipes on the
remote's touchpad generate arrow-key events, which is convenient for apps
that do not process touch directly. These recognizers cancel the underlying
touches when they fire, which interferes with apps that implement their own
handling of the remote touchpad's touch events.

The variable can be set to the following values:

- "0": The swipe gesture recognizers are not installed; raw touch events
  are delivered without being cancelled.
- "1": The swipe gesture recognizers are installed. (default)

This hint should be set before a window is created.

## Version

This hint is available since SDL 3.5.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

