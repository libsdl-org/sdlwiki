###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShowOpenFileDialog

Displays a dialog that lets the user select a file on their filesystem.

## Header File

Defined in [SDL_dialog.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_ShowOpenFileDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const SDL_DialogFileFilter *filters, const char *default_location, SDL_bool allow_many);

```

## Function Parameters

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **callback**             | The function to be invoked when the user selects a file and accepts, or the user cancels the dialog, or an error occurs. The first argument is a null-terminated list of C strings, representing the paths chosen by the user. The list will be empty if the user canceled the dialog, and it will be NULL if an error occured. If an error occured, it can be fetched with [SDL_GetError](SDL_GetError)(). The second argument is the userdata pointer passed to the function. |
| **userdata**             | An optional pointer to pass extra data to the callback when it will be invoked.                                                                                                                                                                                                                                                                                                                                                                                                 |
| **window**               | The window that the dialog should be modal for. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                             |
| **filters**              | A null-terminated list of [SDL_DialogFileFilter](SDL_DialogFileFilter)'s. May be NULL. Not all platforms support this option, and platforms that do support it may allow the user to ignore the filters.                                                                                                                                                                                                                                                                        |
| **default_location**     | The default folder or file to start the dialog at. May be NULL. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                          |
| **allow_many**           | If non-zero, the user will be allowed to select multiple entries. Not all platforms support this option.                                                                                                                                                                                                                                                                                                                                                                        |

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

* [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
* [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

