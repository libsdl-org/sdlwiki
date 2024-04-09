###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ANDROID_TRAP_BACK_BUTTON

A variable to control whether we trap the Android back button to handle it manually.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_ANDROID_TRAP_BACK_BUTTON "SDL_ANDROID_TRAP_BACK_BUTTON"
```

## Remarks

This is necessary for the right mouse button to work on some Android
devices, or to be able to trap the back button for use in your code
reliably. If this hint is true, the back button will show up as an
[SDL_EVENT_KEY_DOWN](SDL_EVENT_KEY_DOWN) /
[SDL_EVENT_KEY_UP](SDL_EVENT_KEY_UP) pair with a keycode of
[SDL_SCANCODE_AC_BACK](SDL_SCANCODE_AC_BACK).

The variable can be set to the following values:

- "0": Back button will be handled as usual for system. (default)
- "1": Back button will be trapped, allowing you to handle the key press
  manually. (This will also let right mouse click work on systems where the
  right mouse button functions as back.)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

