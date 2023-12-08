###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticOpened

Check if the haptic device at the designated index has been opened.

## Syntax

```c
int SDL_HapticOpened(int device_index);

```

## Function Parameters

|                      |                                  |
| -------------------- | -------------------------------- |
| **device_index**     | the index of the device to query |

## Return Value

Returns 1 if it has been opened, 0 if it hasn't or on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticIndex](SDL_HapticIndex.md)
* [SDL_HapticOpen](SDL_HapticOpen.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
