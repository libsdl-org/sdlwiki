###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ALLOW_TOPMOST

If set to "0" then never set the top most bit on a SDL Window, even if the video mode expects it.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ALLOW_TOPMOST "SDL_ALLOW_TOPMOST"
```

## Remarks

This is a debugging aid for developers and not expected to be used by end
users. The default is "1"

This variable can be set to the following values:

- "0": don't allow topmost
- "1": allow topmost

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

