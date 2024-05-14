###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_BMP_SAVE_LEGACY_FORMAT

Prevent SDL from using version 4 of the bitmap header when saving BMPs.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_BMP_SAVE_LEGACY_FORMAT "SDL_BMP_SAVE_LEGACY_FORMAT"
```

## Remarks

The bitmap header version 4 is required for proper alpha channel support
and SDL will use it when required. Should this not be desired, this hint
can force the use of the 40 byte header version which is supported
everywhere.

The variable can be set to the following values:

- "0": Surfaces with a colorkey or an alpha channel are saved to a 32-bit
  BMP file with an alpha mask. SDL will use the bitmap header version 4 and
  set the alpha mask accordingly.
- "1": Surfaces with a colorkey or an alpha channel are saved to a 32-bit
  BMP file without an alpha mask. The alpha channel data will be in the
  file, but applications are going to ignore it.

The default value is "0".

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

