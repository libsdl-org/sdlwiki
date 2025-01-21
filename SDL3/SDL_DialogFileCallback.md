###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DialogFileCallback

Callback used by file dialog functions.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
typedef void (SDLCALL *SDL_DialogFileCallback)(void *userdata, const char * const *filelist, int filter);
```

## Function Parameters

|              |                                                  |
| ------------ | ------------------------------------------------ |
| **userdata** | an app-provided pointer, for the callback's use. |
| **filelist** | the file(s) chosen by the user.                  |
| **filter**   | index of the selected filter.                    |

## Remarks

The specific usage is described in each function.

If `filelist` is:

- NULL, an error occurred. Details can be obtained with
  [SDL_GetError](SDL_GetError)().
- A pointer to NULL, the user either didn't choose any file or canceled the
  dialog.
- A pointer to non-`NULL`, the user chose one or more files. The argument
  is a null-terminated list of pointers to C strings, each containing a
  path.

The filelist argument should not be freed; it will automatically be freed
when the callback returns.

The filter argument is the index of the filter that was selected, or -1 if
no filter was selected or if the platform or method doesn't support
fetching the selected filter.

In Android, the `filelist` are `content://` URIs. They should be opened
using [SDL_IOFromFile](SDL_IOFromFile)() with appropriate modes. This
applies both to open and save file dialog.

## Version

This datatype is available since SDL 3.2.0.

## Code Examples

```c
#include <SDL3/SDL.h>

static const SDL_DialogFileFilter filters[] = {
    { "PNG images",  "png" },
    { "JPEG images", "jpg;jpeg" },
    { "All images",  "png;jpg;jpeg" },
    { "All files",   "*" }
};

static void SDLCALL callback(void* userdata, const char* const* filelist, int filter)
{
    if (!filelist) {
        SDL_Log("An error occured: %s", SDL_GetError());
        return;
    } else if (!*filelist) {
        SDL_Log("The user did not select any file.");
        SDL_Log("Most likely, the dialog was canceled.");
        return;
    }

    while (*filelist) {
        SDL_Log("Full path to selected file: '%s'", *filelist);
        filelist++;
    }

    if (filter < 0) {
        SDL_Log("The current platform does not support fetching "
                "the selected filter, or the user did not select"
                " any filter.");
    } else if (filter < SDL_arraysize(filters)) {
        SDL_Log("The filter selected by the user is '%s' (%s).",
                filters[filter].pattern, filters[filter].name);
    }
}
```

## See Also

- [SDL_DialogFileFilter](SDL_DialogFileFilter)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)
- [SDL_ShowFileDialogWithProperties](SDL_ShowFileDialogWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryDialog](CategoryDialog)

