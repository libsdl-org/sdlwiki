# SDL_GetTouchName

Get the touch device name as reported from the driver or NULL if the index is invalid.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h)

## Syntax

```c
const char* SDL_GetTouchName(int index);
```

## Function Parameters

|     |           |                         |
| --- | --------- | ----------------------- |
| int | **index** | the touch device index. |

## Return Value

(const char *) Returns touch device name, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

