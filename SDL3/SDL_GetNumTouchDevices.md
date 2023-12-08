###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetNumTouchDevices

Get the number of registered touch devices.

## Syntax

```c
int SDL_GetNumTouchDevices(void);

```

## Return Value

Returns the number of registered touch devices.

## Remarks

On some platforms SDL first sees the touch device if it was actually used.
Therefore [SDL_GetNumTouchDevices](SDL_GetNumTouchDevices.md)() may return 0
although devices are available. After using all devices at least once the
number will be correct.

This was fixed for Android in SDL 2.0.1.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTouchDevice](SDL_GetTouchDevice.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryEvents](CategoryEvents.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
