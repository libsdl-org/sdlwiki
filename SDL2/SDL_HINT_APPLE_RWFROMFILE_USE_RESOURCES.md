###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_HINT_APPLE_RWFROMFILE_USE_RESOURCES

Specify if [SDL_RWFromFile](SDL_RWFromFile) should use the resource dir on Apple platforms.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APPLE_RWFROMFILE_USE_RESOURCES "SDL_APPLE_RWFROMFILE_USE_RESOURCES"
```

## Remarks

SDL2 has always done this on Apple platforms, but it can be surprising to
try opening a path to discover that SDL adjusts the path to elsewhere, so
this hint allows that behavior to be disabled.

If running from a App Bundle, this will be MyApp.app/Contents/Resources. If
running as a normal Unix-like process, this will be the directory where the
running binary lives. Setting this hint to 0 avoids this and just uses the
requested path as-is.

This variable can be set to the following values:

- "0": SDL will not use the app resource directory.
- "1": SDL will use the app's resource directory (default).

This hint is available since SDL 2.32.0.

## (This is the legacy documentation for stable SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



## (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

