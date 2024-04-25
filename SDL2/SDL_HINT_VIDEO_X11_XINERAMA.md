###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_X11_XINERAMA

A no-longer-used variable controlling whether the X11 Xinerama extension should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_XINERAMA         "SDL_VIDEO_X11_XINERAMA"
```

## Remarks

Before SDL 2.0.24, this would let apps and users disable Xinerama support
on X11. Now SDL never uses Xinerama, and does not check for this hint at
all. The preprocessor define is left here for source compatibility.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


