###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_FileDialogType

Various types of file dialogs.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
typedef enum SDL_FileDialogType
{
    SDL_FILEDIALOG_OPENFILE,
    SDL_FILEDIALOG_SAVEFILE,
    SDL_FILEDIALOG_OPENFOLDER
} SDL_FileDialogType;
```

## Remarks

This is used by
[SDL_ShowFileDialogWithProperties](SDL_ShowFileDialogWithProperties)() to
decide what kind of dialog to present to the user.

## Version

This enum is available since SDL 3.1.3.

## See Also

- [SDL_ShowFileDialogWithProperties](SDL_ShowFileDialogWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryDialog](CategoryDialog)

