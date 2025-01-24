# SDL_GetMice

Get a list of currently connected mice.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseID * SDL_GetMice(int *count);
```

## Function Parameters

|       |           |                                                                    |
| ----- | --------- | ------------------------------------------------------------------ |
| int * | **count** | a pointer filled in with the number of mice returned, may be NULL. |

## Return Value

([SDL_MouseID](SDL_MouseID) *) Returns a 0 terminated array of mouse
instance IDs or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information. This should be freed with [SDL_free](SDL_free)() when it
is no longer needed.

## Remarks

Note that this will include any device or virtual driver that includes
mouse functionality, including some game controllers, KVM switches, etc.
You should wait for input from a device before you consider it actively in
use.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetMouseNameForID](SDL_GetMouseNameForID)
- [SDL_HasMouse](SDL_HasMouse)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

