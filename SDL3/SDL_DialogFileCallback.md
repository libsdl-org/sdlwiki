###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DialogFileCallback

Callback used by file dialog functions.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
typedef void(SDLCALL *SDL_DialogFileCallback)(void *userdata, const char * const *filelist, int filter);
```

## Remarks

The specific usage is described in each function.

If filelist is... - `NULL`, an error occured. Details can be obtained with
[SDL_GetError](SDL_GetError)(). - A pointer to `NULL`, the user either
didn't choose any file or canceled the dialog. - A pointer to non-`NULL`,
the user chose one or more files. The argument is a null-terminated list of
pointers to C strings, each containing a path.

The filelist argument does not need to be freed; it will automatically be
freed when the callback returns.

The filter argument is the index of the filter that was selected, or one
more than the size of the list (therefore the index of the terminating NULL
entry) if no filter was selected, or -1 if the platform or method doesn't
support fetching the selected filter.

## Code Examples

```c
static void SDLCALL callback(void* userdata, const char* const* files, int filter) {
    if (!files) {
        SDL_Log("An error occured: %s\n", SDL_GetError());
        return;
    }

    if (!*files) {
        SDL_Log("The user did not select any file.\n");
        SDL_Log("Most likely, the dialog was canceled.\n");
        return;
    }

    while (*files) {
        SDL_Log("Full path to selected file: '%s'\n", *files);
        files++;
    }

    if (filter == -1) {
        SDL_Log("The current platform does not support fetching "
                "the selected filter.\n");
    } else {
        if (filter < sizeof(filters) / sizeof(*filters)) {
            SDL_Log("The filter selected by the user is '%s'.\n",
                     filters[filter]);
        } else {
            SDL_Log("The user did not select any filter.\n");
        }
    }
}
```

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_DialogFileFilter](SDL_DialogFileFilter)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

