###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EnumerateStorageDirectory

Enumerate a directory in a storage container through a callback function.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_EnumerateStorageDirectory(SDL_Storage *storage, const char *path, SDL_EnumerateDirectoryCallback callback, void *userdata);
```

## Function Parameters

|                                                                  |              |                                                               |
| ---------------------------------------------------------------- | ------------ | ------------------------------------------------------------- |
| [SDL_Storage](SDL_Storage) *                                     | **storage**  | a storage container.                                          |
| const char *                                                     | **path**     | the path of the directory to enumerate, or NULL for the root. |
| [SDL_EnumerateDirectoryCallback](SDL_EnumerateDirectoryCallback) | **callback** | a function that is called for each entry in the directory.    |
| void *                                                           | **userdata** | a pointer that is passed to `callback`.                       |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function provides every directory entry through an app-provided
callback, called once for each directory entry, until all results have been
provided or the callback returns either
[SDL_ENUM_SUCCESS](SDL_ENUM_SUCCESS) or
[SDL_ENUM_FAILURE](SDL_ENUM_FAILURE).

This will return false if there was a system problem in general, or if a
callback returns [SDL_ENUM_FAILURE](SDL_ENUM_FAILURE). A successful return
means a callback returned [SDL_ENUM_SUCCESS](SDL_ENUM_SUCCESS) to halt
enumeration, or all directory entries were enumerated.

If `path` is NULL, this is treated as a request to enumerate the root of
the storage container's tree. An empty string also works for this.

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c
// Example program
// Use SDL3 to enumerate all directories in title storage

#include <SDL3/SDL_log.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_storage.h>


SDL_EnumerationResult
my_enumerate_dir_callback(void *userdata, const char* dirname, const char* fname)
{
    SDL_Log("dirname: %s | fname: %s", dirname, fname);
    return SDL_ENUM_CONTINUE;
}

int
main(int argc, char** argv)
{
    SDL_Storage *storage = SDL_OpenTitleStorage("", 0);
    if(storage == NULL) {
        SDL_Log("Unable to open storage %s", SDL_GetError());
    }

    if(!SDL_EnumerateStorageDirectory(storage, ".", my_enumerate_dir_callback, NULL)) {
        SDL_Log("There was a system problem or the callback indicated failure.");
    } else {
        SDL_Log("All directories enumerated or the callback halted enumeration.");
    }

    return 0;
}
```

## See Also

- [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

