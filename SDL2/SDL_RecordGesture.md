###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RecordGesture

Begin recording a gesture on a specified touch device or all touch devices.

## Header File

Defined in [SDL_gesture.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gesture.h)

## Syntax

```c
int SDL_RecordGesture(SDL_TouchID touchId);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **touchId**     | the touch device id, or -1 for all touch devices |

## Return Value

Returns 1 on success or 0 if the specified device could not be found.

## Remarks

If the parameter `touchId` is -1 (i.e., all devices), this function will
always return 1, regardless of whether there actually are any devices.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetTouchDevice](SDL_GetTouchDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


