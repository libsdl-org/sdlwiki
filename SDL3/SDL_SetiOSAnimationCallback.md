###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetiOSAnimationCallback

Use this function to set the animation callback on Apple iOS.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_SetiOSAnimationCallback(SDL_Window * window, int interval, SDL_iOSAnimationCallback callback, void *callbackParam);
```

## Function Parameters

|                                                      |                   |                                                               |
| ---------------------------------------------------- | ----------------- | ------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *                           | **window**        | the window for which the animation callback should be set.    |
| int                                                  | **interval**      | the number of frames after which **callback** will be called. |
| [SDL_iOSAnimationCallback](SDL_iOSAnimationCallback) | **callback**      | the function to call for every frame.                         |
| void *                                               | **callbackParam** | a pointer that is passed to `callback`.                       |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The function prototype for `callback` is:

```c
void callback(void* callbackParam);
```

Where its parameter, `callbackParam`, is what was passed as `callbackParam`
to [SDL_SetiOSAnimationCallback](SDL_SetiOSAnimationCallback)().

This function is only available on Apple iOS.

For more information see:

https://wiki.libsdl.org/SDL3/README/ios

Note that if you use the "main callbacks" instead of a standard C `main`
function, you don't have to use this API, as SDL will manage this for you.

Details on main callbacks are here:

https://wiki.libsdl.org/SDL3/README/main-functions

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetiOSEventPump](SDL_SetiOSEventPump)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

