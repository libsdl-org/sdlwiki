###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_TRACKPAD_IS_TOUCH_ONLY

A variable that treats trackpads as touch devices.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_TRACKPAD_IS_TOUCH_ONLY "SDL_TRACKPAD_IS_TOUCH_ONLY"
```

## Remarks

On macOS (and possibly other platforms in the future), SDL will report
touches on a trackpad as mouse input, which is generally what users expect
from this device; however, these are often actually full multitouch-capable
touch devices, so it might be preferable to some apps to treat them as
such.

Setting this hint to true will make the trackpad input report as a
multitouch device instead of a mouse. The default is false.

Note that most platforms don't support this hint. As of 2.24.0, it only
supports MacBooks' trackpads on macOS. Others may follow later.

This hint is checked during [SDL_Init](SDL_Init) and can not be changed
after.

This hint is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

