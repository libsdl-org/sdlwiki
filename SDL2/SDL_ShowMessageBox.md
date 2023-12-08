###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ShowMessageBox

Create a modal message box.

## Syntax

```c
int SDL_ShowMessageBox(const SDL_MessageBoxData *messageboxdata, int *buttonid);

```

## Function Parameters

|                        |                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| **messageboxdata**     | the [SDL_MessageBoxData](SDL_MessageBoxData.md) structure with title, text and other options |
| **buttonid**           | the pointer to which user id of hit button should be copied                               |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

If your needs aren't complex, it might be easier to use
[SDL_ShowSimpleMessageBox](SDL_ShowSimpleMessageBox.md).

This function should be called on the thread that created the parent
window, or on the main thread if the messagebox has no parent. It will
block execution of that thread until the user clicks a button or closes the
messagebox.

This function may be called at any time, even before
[SDL_Init](SDL_Init.md)(). This makes it useful for reporting errors like a
failure to create a renderer or OpenGL context.

On X11, SDL rolls its own dialog box with X11 primitives instead of a
formal toolkit like GTK+ or Qt.

Note that if [SDL_Init](SDL_Init.md)() would fail because there isn't any
available video target, this function is likely to fail for the same
reasons. If this is a concern, check the return value from this function
and fall back to writing to stderr if you can.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_ShowSimpleMessageBox](SDL_ShowSimpleMessageBox.md)

----
[CategoryAPI](CategoryAPI.md)
