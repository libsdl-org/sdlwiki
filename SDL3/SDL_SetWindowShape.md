# SDL_SetWindowShape

Set the shape of a transparent window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowShape(SDL_Window *window, SDL_Surface *shape);
```

## Function Parameters

|                              |            |                                                                                        |
| ---------------------------- | ---------- | -------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *   | **window** | the window.                                                                            |
| [SDL_Surface](SDL_Surface) * | **shape**  | the surface representing the shape of the window, or NULL to remove any current shape. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This sets the alpha channel of a transparent window and any fully
transparent areas are also transparent to mouse clicks. If you are using
something besides the SDL render API, then you are responsible for drawing
the alpha channel of the window to match the shape alpha channel to get
consistent cross-platform results.

The shape is copied inside this function, so you can free it afterwards. If
your shape surface changes, you should call
[SDL_SetWindowShape](SDL_SetWindowShape)() again to update the window. This
is an expensive operation, so should be done sparingly.

The window must have been created with the
[SDL_WINDOW_TRANSPARENT](SDL_WINDOW_TRANSPARENT) flag.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

