###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetTouchDevice

Get the touch ID with the given index.

## Syntax

```c
SDL_TouchID SDL_GetTouchDevice(int index);

```

## Function Parameters

|               |                        |
| ------------- | ---------------------- |
| **index**     | the touch device index |

## Return Value

Returns the touch ID with the given index on success or 0 if the index is
invalid; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetNumTouchDevices](SDL_GetNumTouchDevices)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


