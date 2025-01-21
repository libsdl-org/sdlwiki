###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_WINDOW_ALLOW_TOPMOST

If set to "0" then never set the top-most flag on an SDL Window even if the application requests it.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOW_ALLOW_TOPMOST "SDL_WINDOW_ALLOW_TOPMOST"
```

## Remarks

This is a debugging aid for developers and not expected to be used by end
users.

The variable can be set to the following values:

- "0": don't allow topmost
- "1": allow topmost (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

## See also

- [SDL_WINDOW_ALWAYS_ON_TOP](SDL_WINDOW_ALWAYS_ON_TOP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

