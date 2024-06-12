###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowData

Associate an arbitrary named pointer with a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void* SDL_SetWindowData(SDL_Window * window,
                    const char *name,
                    void *userdata);
```

## Function Parameters

|                            |              |                                          |
| -------------------------- | ------------ | ---------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**   | the window to associate with the pointer |
| const char *               | **name**     | the name of the pointer                  |
| void *                     | **userdata** | the associated pointer                   |

## Return Value

(void *) Returns the previous value associated with `name`.

## Remarks

`name` is case-sensitive.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetWindowData](SDL_GetWindowData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

