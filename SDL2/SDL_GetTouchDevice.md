###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTouchDevice

Get the touch ID with the given index.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h)

## Syntax

```c
SDL_TouchID SDL_GetTouchDevice(int index);
```

## Function Parameters

|     |           |                        |
| --- | --------- | ---------------------- |
| int | **index** | the touch device index |

## Return Value

([SDL_TouchID](SDL_TouchID)) Returns the touch ID with the given index on
success or 0 if the index is invalid; call [SDL_GetError](SDL_GetError)()
for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumTouchDevices](SDL_GetNumTouchDevices)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

