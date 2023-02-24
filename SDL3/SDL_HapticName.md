###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticName

Get the implementation dependent name of a haptic device.

## Syntax

```c
const char* SDL_HapticName(int device_index);

```

## Function Parameters

|                      |                               |
| -------------------- | ----------------------------- |
| **device_index**     | index of the device to query. |

## Return Value

Returns the name of the device or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This can be called before any joysticks are opened. If no name can be
found, this function returns NULL.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_NumHaptics](SDL_NumHaptics)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


