###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_ASSERT

A variable controlling response to [SDL_assert](SDL_assert) failures.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ASSERT "SDL_ASSERT"
```

## Remarks

The variable can be set to the following case-sensitive values:

- "abort": Program terminates immediately.
- "break": Program triggers a debugger breakpoint.
- "retry": Program reruns the [SDL_assert](SDL_assert)'s test again.
- "ignore": Program continues on, ignoring this assertion failure this
  time.
- "always_ignore": Program continues on, ignoring this assertion failure
  for the rest of the run.

Note that [SDL_SetAssertionHandler](SDL_SetAssertionHandler) offers a
programmatic means to deal with assertion failures through a callback, and
this hint is largely intended to be used via environment variables by end
users and automated tools.

This hint should be set before an assertion failure is triggered and can be
changed at any time.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

