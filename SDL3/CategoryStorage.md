# CategoryStorage

The storage API is a high-level API designed to abstract away the portability issues that come up when using something lower-level (in SDL's case, this sits on top of SDL_filesystem). It is significantly more restrictive than a typical filesystem API, for a number of reasons:

1. **What to Access:** A common pitfall with existing filesystem APIs is the assumption that all storage is monolithic. However, many other platforms (game consoles in particular) are more strict about what _type_ of filesystem is being accessed; for example, game content and user data are usually two separate storage devices with entirely different characteristics (and possibly different low-level APIs altogether!).
2. **How to Access:** Another common mistake is applications assuming that all storage is universally writeable - again, many platforms treat game content and user data as two separate storage devices, and only user data is writeable while game content is read-only.
3. **When to Access:** The most common portability issue with filesystem access is _timing_ - you cannot always assume that the storage device is always accessible all of the time, nor can you assume that there are no limits to how long you have access to a particular device.

Consider the following example:

```
void ReadGameData(void)
{
    extern char** fileNames;
    extern size_t numFiles;
    for (size_t i = 0; i < numFiles; i += 1) {
        FILE *data = fopen(fileNames[i], "rwb");
        if (data == NULL) {
            // Something bad happened!
        } else {
            // A bunch of stuff happens here
            fclose(data);
        }
    }
}

void ReadSave(void)
{
    FILE *save = fopen("saves/save0.sav", "rb");
    if (save == NULL) {
        // Something bad happened!
    } else {
        // A bunch of stuff happens here
        fclose(save);
    }
}

void WriteSave(void)
{
    FILE *save = fopen("saves/save0.sav", "wb");
    if (save == NULL) {
        // Something bad happened!
    } else {
        // A bunch of stuff happens here
        fclose(save);
    }
}
```

Going over the bullet points again:

1. **What to Access:** This code accesses a global filesystem; game data and saves are all presumed to be in the game's installation folder.
2. **How to Access:** This code assumes that content paths are writeable, and that save data is also writeable despite being in the same location as the game data.
3. **When to Access:** This code assumes that they can be called at any time, since the filesystem is always accessible and has no limits on how long the filesystem is being accessed.

Due to these assumptions, the filesystem code is not portable and will fail under these common scenarios:

- The game is installed on a device that is read-only, both content loading and game saves will fail or crash outright
- Game/User storage is not implicitly mounted, so no files will be found for either scenario when a platform requires explicitly mounting filesystems
- Save data may not be safe since the I/O is not being flushed or validated, so an error occurring elsewhere in the program may result in missing/corrupted save data

When using, SDL_Storage, these types of problems are virtually impossible to trip over:

```
void ReadGameData(void)
{
    extern char** fileNames;
    extern size_t numFiles;

    SDL_Storage *title = SDL_OpenTitleStorage(NULL, 0);
    if (title == NULL) {
        // Something bad happened!
    }
    while (!SDL_StorageReady(title)) {
        SDL_Delay(1);
    }

    for (size_t i = 0; i < numFiles; i += 1) {
        void* dst;
        Uint64 dstLen = 0;

        if (SDL_GetStorageFileSize(title, fileNames[i], &dstLen) && dstLen > 0) {
            dst = SDL_malloc(dstLen);
            if (SDL_ReadStorageFile(title, fileNames[i], dst, dstLen)) {
                // A bunch of stuff happens here
            } else {
                // Something bad happened!
            }
            SDL_free(dst);
        } else {
            // Something bad happened!
        }
    }

    SDL_CloseStorage(title);
}

void ReadSave(void)
{
    SDL_Storage *user = SDL_OpenUserStorage("libsdl", "Storage Example", 0);
    if (user == NULL) {
        // Something bad happened!
    }
    while (!SDL_StorageReady(user)) {
        SDL_Delay(1);
    }

    Uint64 saveLen = 0;
    if (SDL_GetStorageFileSize(user, "save0.sav", &saveLen) && saveLen > 0) {
        void* dst = SDL_malloc(saveLen);
        if (SDL_ReadStorageFile(user, "save0.sav", dst, saveLen)) {
            // A bunch of stuff happens here
        } else {
            // Something bad happened!
        }
        SDL_free(dst);
    } else {
        // Something bad happened!
    }

    SDL_CloseStorage(user);
}

void WriteSave(void)
{
    SDL_Storage *user = SDL_OpenUserStorage("libsdl", "Storage Example", 0);
    if (user == NULL) {
        // Something bad happened!
    }
    while (!SDL_StorageReady(user)) {
        SDL_Delay(1);
    }

    extern void *saveData; // A bunch of stuff happened here...
    extern Uint64 saveLen;
    if (!SDL_WriteStorageFile(user, "save0.sav", saveData, saveLen)) {
        // Something bad happened!
    }

    SDL_CloseStorage(user);
}
```

Note the improvements that SDL_Storage makes:

1. **What to Access:** This code explicitly reads from a title or user storage device based on the context of the function.
2. **How to Access:** This code explicitly uses either a read or write function based on the context of the function.
3. **When to Access:** This code explicitly opens the device when it needs to, and closes it when it is finished working with the filesystem.

The result is an application that is significantly more robust against the increasing demands of platforms and their filesystems!

A publicly available example of an SDL_Storage backend is the [Steam Cloud](https://partner.steamgames.com/doc/features/cloud) backend - you can initialize Steamworks when starting the program, and then SDL will recognize that Steamworks is initialized and automatically use ISteamRemoteStorage when the application opens user storage. More importantly, when you _open_ storage it knows to begin a "batch" of filesystem operations, and when you _close_ storage it knows to end and flush the batch. This is used by Steam to support [Dynamic Cloud Sync](https://steamcommunity.com/groups/steamworks/announcements/detail/3142949576401813670); users can save data on one PC, put the device to sleep, and then continue playing on another PC (and vice versa) with the save data fully synchronized across all devices, allowing for a seamless experience without having to do full restarts of the program.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryStorage, CategoryAPIFunction -->
- [SDL_CloseStorage](SDL_CloseStorage)
- [SDL_CopyStorageFile](SDL_CopyStorageFile)
- [SDL_CreateStorageDirectory](SDL_CreateStorageDirectory)
- [SDL_EnumerateStorageDirectory](SDL_EnumerateStorageDirectory)
- [SDL_GetStorageFileSize](SDL_GetStorageFileSize)
- [SDL_GetStoragePathInfo](SDL_GetStoragePathInfo)
- [SDL_GetStorageSpaceRemaining](SDL_GetStorageSpaceRemaining)
- [SDL_GlobStorageDirectory](SDL_GlobStorageDirectory)
- [SDL_OpenFileStorage](SDL_OpenFileStorage)
- [SDL_OpenStorage](SDL_OpenStorage)
- [SDL_OpenTitleStorage](SDL_OpenTitleStorage)
- [SDL_OpenUserStorage](SDL_OpenUserStorage)
- [SDL_ReadStorageFile](SDL_ReadStorageFile)
- [SDL_RemoveStoragePath](SDL_RemoveStoragePath)
- [SDL_RenameStoragePath](SDL_RenameStoragePath)
- [SDL_StorageReady](SDL_StorageReady)
- [SDL_WriteStorageFile](SDL_WriteStorageFile)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryStorage, CategoryAPIDatatype -->
- [SDL_Storage](SDL_Storage)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryStorage, CategoryAPIStruct -->
- [SDL_StorageInterface](SDL_StorageInterface)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryStorage, CategoryAPIEnum -->
- (none.)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryStorage, CategoryAPIMacro -->
- (none.)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)


