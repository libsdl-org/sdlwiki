###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_DRIVER

A variable specifying which render driver to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_DRIVER              "SDL_RENDER_DRIVER"
```

## Remarks

If the application doesn't pick a specific renderer to use, this variable
specifies the name of the preferred renderer. If the preferred renderer
can't be initialized, the normal default renderer is used.

This variable is case insensitive and can be set to the following values:
"direct3d" "direct3d11" "direct3d12" "opengl" "opengles2" "opengles"
"metal" "software"

The default varies by platform, but it's the first one in the list that is
available on the current platform.

## Default

By default the first one in the list that is available on the current platform is chosen.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


