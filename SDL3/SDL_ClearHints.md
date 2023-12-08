###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearHints

Clear all hints.

## Syntax

```c
void SDL_ClearHints(void);

```

## Remarks

This function is automatically called during [SDL_Quit](SDL_Quit.md)(), and
deletes all callbacks without calling them and frees all memory associated
with hints. If you're calling this from application code you probably want
to call [SDL_ResetHints](SDL_ResetHints.md)() instead.

This function will be removed from the API the next time we rev the ABI.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_ResetHints](SDL_ResetHints.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md)
