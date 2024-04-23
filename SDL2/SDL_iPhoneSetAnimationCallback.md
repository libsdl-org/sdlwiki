###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_iPhoneSetAnimationCallback

Use this function to set the animation callback on Apple iOS.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

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
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The function prototype for `callback` is:

```c
void callback(void* callbackParam);
```

Where its parameter, `callbackParam`, is what was passed as `callbackParam`
to [SDL_iPhoneSetAnimationCallback](SDL_iPhoneSetAnimationCallback)().

This function is only available on Apple iOS.

For more information see:
https://github.com/libsdl-org/SDL/blob/main/docs/README-ios.md

This functions is also accessible using the macro
[SDL_iOSSetAnimationCallback](SDL_iOSSetAnimationCallback)() since SDL
2.0.4.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_iPhoneSetEventPump](SDL_iPhoneSetEventPump)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


