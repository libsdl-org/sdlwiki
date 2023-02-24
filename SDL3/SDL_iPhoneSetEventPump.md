###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_iPhoneSetEventPump

Use this function to enable or disable the SDL event pump on Apple iOS.

## Syntax

```c
void SDL_iPhoneSetEventPump(SDL_bool enabled);

```

## Function Parameters

|                 |                                                                                     |
| --------------- | ----------------------------------------------------------------------------------- |
| **enabled**     | [SDL_TRUE](SDL_TRUE) to enable the event pump, [SDL_FALSE](SDL_FALSE) to disable it |

## Remarks

This function is only available on Apple iOS.

This functions is also accessible using the macro
[SDL_iOSSetEventPump](SDL_iOSSetEventPump)() since SDL 2.0.4.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_iPhoneSetAnimationCallback](SDL_iPhoneSetAnimationCallback)

----
[CategoryAPI](CategoryAPI), [CategorySystem](CategorySystem), [CategoryDraft](CategoryDraft)


