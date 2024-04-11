###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_FORCE_RAISEWINDOW

A variable controlling whether raising the window should be done more forcefully

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_FORCE_RAISEWINDOW    "SDL_HINT_FORCE_RAISEWINDOW"
```

## Remarks

This variable can be set to the following values: "0" - No forcing (the
default) "1" - Extra level of forcing

At present, this is only an issue under MS Windows, which makes it nearly
impossible to programmatically move a window to the foreground, for
"security" reasons. See http://stackoverflow.com/a/34414846 for a
discussion.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

