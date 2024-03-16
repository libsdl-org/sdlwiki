###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenUserStorage

Opens up a container for a user's unique read/write filesystem.

## Syntax

```c
SDL_Storage* SDL_OpenUserStorage(const char *org, const char *app, SDL_PropertiesID props);

```

## Function Parameters

|               |                                                               |
| ------------- | ------------------------------------------------------------- |
| **org**       | the name of your organization                                 |
| **app**       | the name of your application                                  |
| **props**     | a property list that may contain backend-specific information |

## Return Value

Returns a user storage container on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

While title storage can generally be kept open throughout runtime, user
storage should only be opened when the client is ready to read/write files.
This allows the backend to properly batch R/W operations and flush them
when the container has been closed; ensuring safe and optimal save I/O.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenTitleStorage](SDL_OpenTitleStorage)
* [SDL_OpenStorage](SDL_OpenStorage)
* [SDL_CloseStorage](SDL_CloseStorage)
* [SDL_StorageReady](SDL_StorageReady)
* [SDL_StorageFileSize](SDL_StorageFileSize)
* [SDL_StorageReadFile](SDL_StorageReadFile)
* [SDL_StorageWriteFile](SDL_StorageWriteFile)
* [SDL_StorageSpaceRemaining](SDL_StorageSpaceRemaining)

----
[CategoryAPI](CategoryAPI)

