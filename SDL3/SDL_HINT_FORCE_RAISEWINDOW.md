###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_FORCE_RAISEWINDOW

A variable controlling whether raising the window should be done more forcefully.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_FORCE_RAISEWINDOW    "SDL_FORCE_RAISEWINDOW"
```

## Remarks

The variable can be set to the following values:

- "0": Honor the OS policy for raising windows. (default)
- "1": Force the window to be raised, overriding any OS policy.

At present, this is only an issue under MS Windows, which makes it nearly
impossible to programmatically move a window to the foreground, for
"security" reasons. See http://stackoverflow.com/a/34414846 for a
discussion.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

