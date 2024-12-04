###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ShowOpenFileDialog

Displays a dialog that lets the user select a file on their filesystem.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
void SDL_ShowOpenFileDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const SDL_DialogFileFilter *filters, int nfilters, const char *default_location, bool allow_many);
```

## Function Parameters

|                                                      |                      |                                                                                                                                                                                                                             |
| ---------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_DialogFileCallback](SDL_DialogFileCallback)     | **callback**         | a function pointer to be invoked when the user selects a file and accepts, or cancels the dialog, or an error occurs.                                                                                                       |
| void *                                               | **userdata**         | an optional pointer to pass extra data to the callback when it will be invoked.                                                                                                                                             |
| [SDL_Window](SDL_Window) *                           | **window**           | the window that the dialog should be modal for, may be NULL. Not all platforms support this option.                                                                                                                         |
| const [SDL_DialogFileFilter](SDL_DialogFileFilter) * | **filters**          | a list of filters, may be NULL. Not all platforms support this option, and platforms that do support it may allow the user to ignore the filters. If non-NULL, it must remain valid at least until the callback is invoked. |
| int                                                  | **nfilters**         | the number of filters. Ignored if filters is NULL.                                                                                                                                                                          |
| const char *                                         | **default_location** | the default folder or file to start the dialog at, may be NULL. Not all platforms support this option.                                                                                                                      |
| bool                                                 | **allow_many**       | if non-zero, the user will be allowed to select multiple entries. Not all platforms support this option.                                                                                                                    |

## Remarks

This is an asynchronous function; it will return immediately, and the
result will be passed to the callback.

The callback will be invoked with a null-terminated list of files the user
chose. The list will be empty if the user canceled the dialog, and it will
be NULL if an error occurred.

Note that the callback may be called from a different thread than the one
the function was invoked on.

Depending on the platform, the user may be allowed to input paths that
don't yet exist.

On Linux, dialogs may require XDG Portals, which requires DBus, which
requires an event-handling loop. Apps that do not use SDL to handle events
should add a call to [SDL_PumpEvents](SDL_PumpEvents) in their main loop.

## Thread Safety

This function should be called only from the main thread. The callback may
be invoked from the same thread or from a different one, depending on the
OS's constraints.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_DialogFileCallback](SDL_DialogFileCallback)
- [SDL_DialogFileFilter](SDL_DialogFileFilter)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)
- [SDL_ShowFileDialogWithProperties](SDL_ShowFileDialogWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryDialog](CategoryDialog)

