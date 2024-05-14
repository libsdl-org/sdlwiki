###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StorageInterface

Function interface for [SDL_Storage](SDL_Storage).

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
typedef struct SDL_StorageInterface
{
    /* Called when the storage is closed */
    int (SDLCALL *close)(void *userdata);

    /* Optional, returns whether the storage is currently ready for access */
    SDL_bool (SDLCALL *ready)(void *userdata);

    /* Enumerate a directory, optional for write-only storage */
    int (SDLCALL *enumerate)(void *userdata, const char *path, SDL_EnumerateDirectoryCallback callback, void *callback_userdata);

    /* Get path information, optional for write-only storage */
    int (SDLCALL *info)(void *userdata, const char *path, SDL_PathInfo *info);

    /* Read a file from storage, optional for write-only storage */
    int (SDLCALL *read_file)(void *userdata, const char *path, void *destination, Uint64 length);

    /* Write a file to storage, optional for read-only storage */
    int (SDLCALL *write_file)(void *userdata, const char *path, const void *source, Uint64 length);

    /* Create a directory, optional for read-only storage */
    int (SDLCALL *mkdir)(void *userdata, const char *path);

    /* Remove a file or empty directory, optional for read-only storage */
    int (SDLCALL *remove)(void *userdata, const char *path);

    /* Rename a path, optional for read-only storage */
    int (SDLCALL *rename)(void *userdata, const char *oldpath, const char *newpath);

    /* Get the space remaining, optional for read-only storage */
    Uint64 (SDLCALL *space_remaining)(void *userdata);
} SDL_StorageInterface;
```

## Remarks

Apps that want to supply a custom implementation of
[SDL_Storage](SDL_Storage) will fill in all the functions in this struct,
and then pass it to [SDL_OpenStorage](SDL_OpenStorage) to create a custom
[SDL_Storage](SDL_Storage) object.

It is not usually necessary to do this; SDL provides standard
implementations for many things you might expect to do with an
[SDL_Storage](SDL_Storage).

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStorage](CategoryStorage)

