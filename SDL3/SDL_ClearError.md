# SDL_ClearError

Clear any previous error message for this thread.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
bool SDL_ClearError(void);
```

## Return Value

(bool) Returns true.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
const char *error = SDL_GetError();
if (*error) {
  SDL_Log("SDL error: %s", error);
  SDL_ClearError();
}
```

## See Also

- [SDL_GetError](SDL_GetError)
- [SDL_SetError](SDL_SetError)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

