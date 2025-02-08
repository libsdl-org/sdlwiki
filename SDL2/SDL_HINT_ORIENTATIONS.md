# SDL_HINT_ORIENTATIONS

A variable controlling which orientations are allowed on iOS/Android.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ORIENTATIONS "SDL_IOS_ORIENTATIONS"
```

## Remarks

In some circumstances it is necessary to be able to explicitly control
which UI orientations are allowed.

This variable is a space delimited list of the following values:

- "LandscapeLeft"
- "LandscapeRight"
- "Portrait"
- "PortraitUpsideDown"

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

