# SDL_GDKResumeRenderer

Call this to resume Render operations on Xbox after receiving the [SDL_EVENT_WILL_ENTER_FOREGROUND](SDL_EVENT_WILL_ENTER_FOREGROUND) event.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_GDKResumeRenderer(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                                             |
| ------------------------------ | ------------ | ------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should resume operation. |

## Remarks

When resuming, this function MUST be called before calling any other
[SDL_Render](SDL_Render) functions.

This function MUST be called on the application's render thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

