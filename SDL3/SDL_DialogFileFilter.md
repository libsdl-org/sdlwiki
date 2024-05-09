###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DialogFileFilter

An entry for filters for file dialogs.

## Header File

Defined in [<SDL3/SDL_dialog.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_dialog.h)

## Syntax

```c
typedef struct SDL_DialogFileFilter
{
    const char *name;
    const char *pattern;
} SDL_DialogFileFilter;
```

## Remarks

`name` is a user-readable label for the filter (for example, "Office
document").

`pattern` is a semicolon-separated list of file extensions (for example,
"doc;docx"). File extensions may only contain alphanumeric characters,
hyphens, underscores and periods. Alternatively, the whole string can be a
single asterisk ("*"), which serves as an "All files" filter.

## Code Examples

This structure is most often used as a **NULL-terminated** array:

```c
const SDL_DialogFileFilter filters[] = {
    { "PNG images",  "png" },
    { "JPEG images", "jgp;jpeg" },
    { "All images",  "png;jpg;jpeg" },
    { "All files",   "*" },
    { NULL, NULL }
};
```

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_DialogFileCallback](SDL_DialogFileCallback)
- [SDL_ShowOpenFileDialog](SDL_ShowOpenFileDialog)
- [SDL_ShowSaveFileDialog](SDL_ShowSaveFileDialog)
- [SDL_ShowOpenFolderDialog](SDL_ShowOpenFolderDialog)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

