###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_iPhoneSetAnimationCallback

Use this function to set the animation callback on Apple iOS.

## Syntax

```c
int SDL_iPhoneSetAnimationCallback(SDL_Window * window, int interval, void (SDLCALL *callback)(void*), void *callbackParam);

```

## Function Parameters

|                       |                                                              |
| --------------------- | ------------------------------------------------------------ |
| **window**            | the window for which the animation callback should be set    |
| **interval**          | the number of frames after which **callback** will be called |
| **callback**          | the function to call for every frame.                        |
| **callbackParam**     | a pointer that is passed to `callback`.                      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The function prototype for `callback` is:

```c
void callback(void* callbackParam);
```

Where its parameter, `callbackParam`, is what was passed as `callbackParam`
to [SDL_iPhoneSetAnimationCallback](SDL_iPhoneSetAnimationCallback.md)().

This function is only available on Apple iOS.

For more information see:
https://github.com/libsdl-org/SDL/blob/main/docs/README-ios.md

This functions is also accessible using the macro
[SDL_iOSSetAnimationCallback](SDL_iOSSetAnimationCallback.md)() since SDL
2.0.4.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_iPhoneSetEventPump](SDL_iPhoneSetEventPump.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySystem](CategorySystem.md), [CategoryDraft](CategoryDraft.md)
