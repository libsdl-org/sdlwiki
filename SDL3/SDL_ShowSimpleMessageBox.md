###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowSimpleMessageBox

Display a simple modal message box.

## Header File

Defined in [<SDL3/SDL_messagebox.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
int SDL_ShowSimpleMessageBox(SDL_MessageBoxFlags flags, const char *title, const char *message, SDL_Window *window);
```

## Function Parameters

|                                            |             |                                                      |
| ------------------------------------------ | ----------- | ---------------------------------------------------- |
| [SDL_MessageBoxFlags](SDL_MessageBoxFlags) | **flags**   | an [SDL_MessageBoxFlags](SDL_MessageBoxFlags) value. |
| const char *                               | **title**   | uTF-8 title text.                                    |
| const char *                               | **message** | uTF-8 message text.                                  |
| [SDL_Window](SDL_Window) *                 | **window**  | the parent window, or NULL for no parent.            |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If your needs aren't complex, this function is preferred over
[SDL_ShowMessageBox](SDL_ShowMessageBox).

`flags` may be any of the following:

- [`SDL_MESSAGEBOX_ERROR`](SDL_MESSAGEBOX_ERROR): error dialog
- [`SDL_MESSAGEBOX_WARNING`](SDL_MESSAGEBOX_WARNING): warning dialog
- [`SDL_MESSAGEBOX_INFORMATION`](SDL_MESSAGEBOX_INFORMATION): informational
  dialog

This function should be called on the thread that created the parent
window, or on the main thread if the messagebox has no parent. It will
block execution of that thread until the user clicks a button or closes the
messagebox.

This function may be called at any time, even before
[SDL_Init](SDL_Init)(). This makes it useful for reporting errors like a
failure to create a renderer or OpenGL context.

On X11, SDL rolls its own dialog box with X11 primitives instead of a
formal toolkit like GTK+ or Qt.

Note that if [SDL_Init](SDL_Init)() would fail because there isn't any
available video target, this function is likely to fail for the same
reasons. If this is a concern, check the return value from this function
and fall back to writing to stderr if you can.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_ERROR,
                         "Missing file",
                         "File is missing. Please reinstall the program.",
                         NULL);
```

## See Also

- [SDL_ShowMessageBox](SDL_ShowMessageBox)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMessagebox](CategoryMessagebox)

