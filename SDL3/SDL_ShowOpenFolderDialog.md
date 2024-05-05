###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowOpenFolderDialog

Displays a dialog that lets the user select a folder on their filesystem.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
void SDL_ShowOpenFolderDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const char *default_location, SDL_bool allow_many);

```

## Function Parameters

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **callback**             | An [SDL_DialogFileCallback](SDL_DialogFileCallback) to be invoked when the user selects a file and accepts, or cancels the dialog, or an error occurs. The first argument is a null-terminated list of C strings, representing the paths chosen by the user. The list will be empty if the user canceled the dialog, and it will be NULL if an error occured. If an error occured, it can be fetched with [SDL_GetError](SDL_GetError)(). The second argument is the userdata pointer passed to the function. The third argument is always -1 for [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog). |
| **userdata**             | An optional pointer to pass extra data to the callback when it will be invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **window**               | The window that the dialog should be modal for. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **default_location**     | The default folder or file to start the dialog at. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **allow_many**           | If non-zero, the user will be allowed to select multiple entries. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Remarks

This function should only be invoked from the main thread.

This is an asynchronous function; it will return immediately, and the
result will be passed to the callback.

The callback will be invoked with a null-terminated list of files the user
chose. The list will be empty if the user canceled the dialog, and it will
be NULL if an error occured.

Note that the callback may be called from a different thread than the one
the function was invoked on.

Depending on the platform, the user may be allowed to input paths that
don't yet exist.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DialogFileCallback](SDL_DialogFileCallback)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

