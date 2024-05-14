###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowSaveFileDialog

Displays a dialog that lets the user choose a new or existing file on their filesystem.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
void SDL_ShowSaveFileDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const SDL_DialogFileFilter *filters, const char *default_location);

```

## Function Parameters

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **callback**             | An [SDL_DialogFileCallback](SDL_DialogFileCallback) to be invoked when the user selects a file and accepts, or cancels the dialog, or an error occurs. The first argument is a null-terminated list of C strings, representing the paths chosen by the user. The list will be empty if the user canceled the dialog, and it will be NULL if an error occured. If an error occured, it can be fetched with [SDL_GetError](SDL_GetError)(). The second argument is the userdata pointer passed to the function. The third argument is the index of the filter selected by the user, or one past the index of the last filter (therefore the index of the terminating NULL filter) if no filter was chosen, or -1 if the platform does not support detecting the selected filter. |
| **userdata**             | An optional pointer to pass extra data to the callback when it will be invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **window**               | The window that the dialog should be modal for. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **filters**              | A null-terminated list of [SDL_DialogFileFilter](SDL_DialogFileFilter)'s. May be NULL. Not all platforms support this option, and platforms that do support it may allow the user to ignore the filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **default_location**     | The default folder or file to start the dialog at. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Remarks

This function should only be invoked from the main thread.

This is an asynchronous function; it will return immediately, and the
result will be passed to the callback.

The callback will be invoked with a null-terminated list of files the user
chose. The list will be empty if the user canceled the dialog, and it will
be NULL if an error occured.

Note that the callback may be called from a different thread than the one
the function was invoked on.

The chosen file may or may not already exist.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DialogFileCallback](SDL_DialogFileCallback)
- [SDL_DialogFileFilter](SDL_DialogFileFilter)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryDialog](CategoryDialog)

