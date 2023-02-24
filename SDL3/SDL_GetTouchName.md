###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTouchName

Get the touch device name as reported from the driver or NULL if the index is invalid.

## Syntax

```c
const char* SDL_GetTouchName(int index);

```

## Function Parameters

|               |                        |
| ------------- | ---------------------- |
| **index**     | the touch device index |

## Return Value

Returns touch device name

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

