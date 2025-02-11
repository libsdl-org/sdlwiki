# SDL_HINT_ANDROID_TRAP_BACK_BUTTON

A variable to control whether we trap the Android back button to handle it manually.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_TRAP_BACK_BUTTON "SDL_ANDROID_TRAP_BACK_BUTTON"
```

## Remarks

This is necessary for the right mouse button to work on some Android
devices, or to be able to trap the back button for use in your code
reliably. If set to true, the back button will show up as an
[SDL_KEYDOWN](SDL_KEYDOWN) / [SDL_KEYUP](SDL_KEYUP) pair with a keycode of
[SDL_SCANCODE_AC_BACK](SDL_SCANCODE_AC_BACK).

The variable can be set to the following values:

- "0": Back button will be handled as usual for system. (default)
- "1": Back button will be trapped, allowing you to handle the key press
  manually. (This will also let right mouse click work on systems where the
  right mouse button functions as back.)

The value of this hint is used at runtime, so it can be changed at any
time.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

