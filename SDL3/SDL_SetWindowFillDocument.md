# SDL_SetWindowFillDocument

Set the window to fill the current document space (Emscripten only).

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowFillDocument(SDL_Window *window, bool fill);
```

## Function Parameters

|                            |            |                                                                |
| -------------------------- | ---------- | -------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window of which to change the fill-document state.         |
| bool                       | **fill**   | true to set the window to fill the document, false to disable. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_FILL_DOCUMENT`](SDL_WINDOW_FILL_DOCUMENT) flag.

Currently this flag only applies to the Emscripten target.

When enabled, the canvas element fills the entire document. Resize events
will be generated as the browser window is resized, as that will adjust the
canvas size as well. The canvas will cover anything else on the page,
including any controls provided by Emscripten in its generated HTML file
(in fact, any elements on the page that aren't the canvas will be moved
into a hidden `div` element).

Often times this is desirable for a browser-based game, but it means
several things that we expect of an SDL window on other platforms might not
work as expected, such as minimum window sizes and aspect ratios.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

