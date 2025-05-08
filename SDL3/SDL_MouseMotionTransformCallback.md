# SDL_MouseMotionTransformCallback

A callback used to transform mouse motion delta from raw values.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
typedef void (SDLCALL *SDL_MouseMotionTransformCallback)( void *userdata, Uint64 timestamp, SDL_Window *window, SDL_MouseID mouseID, float *x, float *y);
```

## Function Parameters

|               |                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------- |
| **userdata**  | what was passed as `userdata` to [SDL_SetRelativeMouseTransform](SDL_SetRelativeMouseTransform)(). |
| **timestamp** | the associated time at which this mouse motion event was received.                                 |
| **window**    | the associated window to which this mouse motion event was addressed.                              |
| **mouseID**   | the associated mouse from which this mouse motion event was emitted.                               |
| **x**         | pointer to a variable that will be treated as the resulting x-axis motion.                         |
| **y**         | pointer to a variable that will be treated as the resulting y-axis motion.                         |

## Remarks

This is called during SDL's handling of platform mouse events to scale the
values of the resulting motion delta.

## Thread Safety

This callback is called by SDL's internal mouse input processing procedure,
which may be a thread separate from the main event loop that is run at
realtime priority. Stalling this thread with too much work in the callback
can therefore potentially freeze the entire system. Care should be taken
with proper synchronization practices when adding other side effects beyond
mutation of the x and y values.

## Version

This datatype is available since SDL 3.4.0.

## See Also

- [SDL_SetRelativeMouseTransform](SDL_SetRelativeMouseTransform)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryMouse](CategoryMouse)

