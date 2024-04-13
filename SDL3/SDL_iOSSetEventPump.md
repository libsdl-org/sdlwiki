###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_iOSSetEventPump

Use this function to enable or disable the SDL event pump on Apple iOS.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_iOSSetEventPump(SDL_bool enabled);

```

## Function Parameters

|                 |                                                                                     |
| --------------- | ----------------------------------------------------------------------------------- |
| **enabled**     | [SDL_TRUE](SDL_TRUE) to enable the event pump, [SDL_FALSE](SDL_FALSE) to disable it |

## Remarks

This function is only available on Apple iOS.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_iOSSetAnimationCallback](SDL_iOSSetAnimationCallback)


## SDL_iPhoneSetEventPump

Use this function to enable or disable the SDL event pump on Apple iOS.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem), [CategoryDraft](CategoryDraft)


