###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenTitleStorage

Opens up a read-only container for the application's filesystem.

## Syntax

```c
SDL_Storage* SDL_OpenTitleStorage(const char *override, SDL_PropertiesID props);

```

## Function Parameters

|                  |                                                               |
| ---------------- | ------------------------------------------------------------- |
| **override**     | a path to override the backend's default title root           |
| **props**        | a property list that may contain backend-specific information |

## Return Value

Returns a title storage container on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenUserStorage](SDL_OpenUserStorage)
* [SDL_OpenStorage](SDL_OpenStorage)
* [SDL_TitleStorageReady](SDL_TitleStorageReady)
* [SDL_CloseStorage](SDL_CloseStorage)
* [SDL_StorageReady](SDL_StorageReady)
* [SDL_StorageFileSize](SDL_StorageFileSize)
* [SDL_StorageReadFile](SDL_StorageReadFile)
* [SDL_StorageWriteFile](SDL_StorageWriteFile)
* [SDL_StorageSpaceRemaining](SDL_StorageSpaceRemaining)

----
[CategoryAPI](CategoryAPI)

