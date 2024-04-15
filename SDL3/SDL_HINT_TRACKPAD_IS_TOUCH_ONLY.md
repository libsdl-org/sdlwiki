###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_TRACKPAD_IS_TOUCH_ONLY

A variable controlling whether trackpads should be treated as touch devices.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

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

The variable can be set to the following values:

- "0": Trackpad will send mouse events. (default)
- "1": Trackpad will send touch events.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

