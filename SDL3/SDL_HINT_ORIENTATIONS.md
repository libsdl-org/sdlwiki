###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ORIENTATIONS

A variable controlling which orientations are allowed on iOS/Android.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ORIENTATIONS "SDL_ORIENTATIONS"
```

## Remarks

In some circumstances it is necessary to be able to explicitly control
which UI orientations are allowed.

This variable is a space delimited list of the following values:

- "LandscapeLeft"
- "LandscapeRight"
- "Portrait"
- "PortraitUpsideDown"

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]


