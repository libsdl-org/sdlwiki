###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClearError

Clear any previous error message for this thread.

## Syntax

```c
void SDL_ClearError(void);

```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
const char *error = SDL_GetError();
if (*error) {
  SDL_Log("SDL error: %s", error);
  SDL_ClearError();
}
```

## Related Functions

* [SDL_GetError](SDL_GetError.md)
* [SDL_SetError](SDL_SetError.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryError](CategoryError.md)
