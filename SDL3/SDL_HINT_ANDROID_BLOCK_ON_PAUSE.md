# SDL_HINT_ANDROID_BLOCK_ON_PAUSE

A variable to control whether the event loop will block itself when the app is paused.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_BLOCK_ON_PAUSE "SDL_ANDROID_BLOCK_ON_PAUSE"
```

## Remarks

The variable can be set to the following values:

- "0": Non blocking.
- "1": Blocking. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

