# SDL_SetiOSEventPump

Use this function to enable or disable the SDL event pump on Apple iOS.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
void SDL_SetiOSEventPump(bool enabled);
```

## Function Parameters

|      |             |                                                     |
| ---- | ----------- | --------------------------------------------------- |
| bool | **enabled** | true to enable the event pump, false to disable it. |

## Remarks

This function is only available on Apple iOS.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetiOSAnimationCallback](SDL_SetiOSAnimationCallback)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

