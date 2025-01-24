# SDL_HINT_FORCE_RAISEWINDOW

A variable controlling whether raising the window should be done more forcefully

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_FORCE_RAISEWINDOW    "SDL_HINT_FORCE_RAISEWINDOW"
```

## Remarks

This variable can be set to the following values:

- "0": No forcing (the default)
- "1": Extra level of forcing

At present, this is only an issue under MS Windows, which makes it nearly
impossible to programmatically move a window to the foreground, for
"security" reasons. See http://stackoverflow.com/a/34414846 for a
discussion.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

