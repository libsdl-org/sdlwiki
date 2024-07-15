###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetiOSEventPump

Use this function to enable or disable the SDL event pump on Apple iOS.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
void SDL_SetiOSEventPump(SDL_bool enabled);
```

## Function Parameters

|                      |             |                                                                                      |
| -------------------- | ----------- | ------------------------------------------------------------------------------------ |
| [SDL_bool](SDL_bool) | **enabled** | [SDL_TRUE](SDL_TRUE) to enable the event pump, [SDL_FALSE](SDL_FALSE) to disable it. |

## Remarks

This function is only available on Apple iOS.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetiOSAnimationCallback](SDL_SetiOSAnimationCallback)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

