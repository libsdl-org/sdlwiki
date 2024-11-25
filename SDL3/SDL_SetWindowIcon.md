###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowIcon

Set the icon for a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowIcon(SDL_Window *window, SDL_Surface *icon);
```

## Function Parameters

|                              |            |                                                                             |
| ---------------------------- | ---------- | --------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *   | **window** | the window to change.                                                       |
| [SDL_Surface](SDL_Surface) * | **icon**   | an [SDL_Surface](SDL_Surface) structure containing the icon for the window. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If this function is passed a surface with alternate representations, the
surface will be interpreted as the content to be used for 100% display
scale, and the alternate representations will be used for high DPI
situations. For example, if the original surface is 32x32, then on a 2x
macOS display or 200% display scale on Windows, a 64x64 version of the
image will be used, if available. If a matching version of the image isn't
available, the closest larger size image will be downscaled to the
appropriate size and be used instead, if available. Otherwise, the closest
smaller image will be upscaled and be used instead.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

