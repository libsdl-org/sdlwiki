# SDL_GDKSuspendRenderer

Call this to suspend Render operations on Xbox after receiving the [SDL_EVENT_DID_ENTER_BACKGROUND](SDL_EVENT_DID_ENTER_BACKGROUND) event.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
void SDL_GDKSuspendRenderer(SDL_Renderer *renderer);
```

## Function Parameters

|                                |              |                                              |
| ------------------------------ | ------------ | -------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should suspend operation. |

## Remarks

Do NOT call any [SDL_Render](SDL_Render) functions after calling this
function! This must also be called before calling
[SDL_GDKSuspendComplete](SDL_GDKSuspendComplete).

This function MUST be called on the application's render thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

