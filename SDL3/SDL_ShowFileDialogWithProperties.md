# SDL_ShowFileDialogWithProperties

Create and launch a file dialog with the specified properties.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
void SDL_ShowFileDialogWithProperties(SDL_FileDialogType type, SDL_DialogFileCallback callback, void *userdata, SDL_PropertiesID props);
```

## Function Parameters

|                                                  |              |                                                                                                                       |
| ------------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| [SDL_FileDialogType](SDL_FileDialogType)         | **type**     | the type of file dialog.                                                                                              |
| [SDL_DialogFileCallback](SDL_DialogFileCallback) | **callback** | a function pointer to be invoked when the user selects a file and accepts, or cancels the dialog, or an error occurs. |
| void *                                           | **userdata** | an optional pointer to pass extra data to the callback when it will be invoked.                                       |
| [SDL_PropertiesID](SDL_PropertiesID)             | **props**    | the properties to use.                                                                                                |

## Remarks

These are the supported properties:

- [`SDL_PROP_FILE_DIALOG_FILTERS_POINTER`](SDL_PROP_FILE_DIALOG_FILTERS_POINTER):
  a pointer to a list of [SDL_DialogFileFilter](SDL_DialogFileFilter)
  structs, which will be used as filters for file-based selections. Ignored
  if the dialog is an "Open Folder" dialog. If non-NULL, the array of
  filters must remain valid at least until the callback is invoked.
- [`SDL_PROP_FILE_DIALOG_NFILTERS_NUMBER`](SDL_PROP_FILE_DIALOG_NFILTERS_NUMBER):
  the number of filters in the array of filters, if it exists.
- [`SDL_PROP_FILE_DIALOG_WINDOW_POINTER`](SDL_PROP_FILE_DIALOG_WINDOW_POINTER):
  the window that the dialog should be modal for.
- [`SDL_PROP_FILE_DIALOG_LOCATION_STRING`](SDL_PROP_FILE_DIALOG_LOCATION_STRING):
  the default folder or file to start the dialog at.
- [`SDL_PROP_FILE_DIALOG_MANY_BOOLEAN`](SDL_PROP_FILE_DIALOG_MANY_BOOLEAN):
  true to allow the user to select more than one entry.
- [`SDL_PROP_FILE_DIALOG_TITLE_STRING`](SDL_PROP_FILE_DIALOG_TITLE_STRING):
  the title for the dialog.
- [`SDL_PROP_FILE_DIALOG_ACCEPT_STRING`](SDL_PROP_FILE_DIALOG_ACCEPT_STRING):
  the label that the accept button should have.
- [`SDL_PROP_FILE_DIALOG_CANCEL_STRING`](SDL_PROP_FILE_DIALOG_CANCEL_STRING):
  the label that the cancel button should have.

Note that each platform may or may not support any of the properties.

## Thread Safety

This function should be called only from the main thread. The callback may
be invoked from the same thread or from a different one, depending on the
OS's constraints.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_FileDialogType](SDL_FileDialogType)
- [SDL_DialogFileCallback](SDL_DialogFileCallback)
- [SDL_DialogFileFilter](SDL_DialogFileFilter)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryDialog](CategoryDialog)

