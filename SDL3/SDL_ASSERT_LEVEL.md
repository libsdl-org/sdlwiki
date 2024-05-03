###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ASSERT_LEVEL

The level of assertion aggressiveness.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_ASSERT_LEVEL SomeNumberBasedOnVariousFactors
```

## Remarks

This value changes depending on compiler options and other preprocessor
defines.

It is currently one of the following values, but future SDL releases might
add more:

- 0: All SDL assertion macros are disabled.
- 1: Release settings: [SDL_assert](SDL_assert) disabled,
  [SDL_assert_release](SDL_assert_release) enabled.
- 2: Debug settings: [SDL_assert](SDL_assert) and
  [SDL_assert_release](SDL_assert_release) enabled.
- 3: Paranoid settings: All SDL assertion macros enabled, including
  [SDL_assert_paranoid](SDL_assert_paranoid).

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

