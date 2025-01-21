###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetMouseNameForID

Get the name of a mouse.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
const char * SDL_GetMouseNameForID(SDL_MouseID instance_id);
```

## Function Parameters

|                            |                 |                        |
| -------------------------- | --------------- | ---------------------- |
| [SDL_MouseID](SDL_MouseID) | **instance_id** | the mouse instance ID. |

## Return Value

(const char *) Returns the name of the selected mouse, or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns "" if the mouse doesn't have a name.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetMice](SDL_GetMice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

