# SDL_SetRelativeMouseTransform

Set a user-defined function by which to transform relative mouse inputs.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_SetRelativeMouseTransform(SDL_MouseMotionTransformCallback callback, void *userdata);
```

## Function Parameters

|                                                                      |              |                                                                                   |
| -------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------- |
| [SDL_MouseMotionTransformCallback](SDL_MouseMotionTransformCallback) | **callback** | a callback used to transform relative mouse motion, or NULL for default behavior. |
| void *                                                               | **userdata** | a pointer that will be passed to `callback`.                                      |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This overrides the relative system scale and relative speed scale hints.
Should be called prior to enabling relative mouse mode, fails otherwise.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

