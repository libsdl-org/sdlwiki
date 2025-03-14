# SDL_Folder

The type of the OS-provided default folder for a specific purpose.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
typedef enum SDL_Folder
{
    SDL_FOLDER_HOME,        /**< The folder which contains all of the current user's data, preferences, and documents. It usually contains most of the other folders. If a requested folder does not exist, the home folder can be considered a safe fallback to store a user's documents. */
    SDL_FOLDER_DESKTOP,     /**< The folder of files that are displayed on the desktop. Note that the existence of a desktop folder does not guarantee that the system does show icons on its desktop; certain GNU/Linux distros with a graphical environment may not have desktop icons. */
    SDL_FOLDER_DOCUMENTS,   /**< User document files, possibly application-specific. This is a good place to save a user's projects. */
    SDL_FOLDER_DOWNLOADS,   /**< Standard folder for user files downloaded from the internet. */
    SDL_FOLDER_MUSIC,       /**< Music files that can be played using a standard music player (mp3, ogg...). */
    SDL_FOLDER_PICTURES,    /**< Image files that can be displayed using a standard viewer (png, jpg...). */
    SDL_FOLDER_PUBLICSHARE, /**< Files that are meant to be shared with other users on the same computer. */
    SDL_FOLDER_SAVEDGAMES,  /**< Save files for games. */
    SDL_FOLDER_SCREENSHOTS, /**< Application screenshots. */
    SDL_FOLDER_TEMPLATES,   /**< Template files to be used when the user requests the desktop environment to create a new file in a certain folder, such as "New Text File.txt".  Any file in the Templates folder can be used as a starting point for a new file. */
    SDL_FOLDER_VIDEOS,      /**< Video files that can be played using a standard video player (mp4, webm...). */
    SDL_FOLDER_COUNT        /**< Total number of types in this enum, not a folder type by itself. */
} SDL_Folder;
```

## Remarks

Note that the Trash folder isn't included here, because trashing files
usually involves extra OS-specific functionality to remember the file's
original location.

The folders supported per platform are:

|             | Windows | macOS/iOS | tvOS | Unix (XDG) | Haiku | Emscripten |
| ----------- | ------- | --------- | ---- | ---------- | ----- | ---------- |
| HOME        | X       | X         |      | X          | X     | X          |
| DESKTOP     | X       | X         |      | X          | X     |            |
| DOCUMENTS   | X       | X         |      | X          |       |            |
| DOWNLOADS   | Vista+  | X         |      | X          |       |            |
| MUSIC       | X       | X         |      | X          |       |            |
| PICTURES    | X       | X         |      | X          |       |            |
| PUBLICSHARE |         | X         |      | X          |       |            |
| SAVEDGAMES  | Vista+  |           |      |            |       |            |
| SCREENSHOTS | Vista+  |           |      |            |       |            |
| TEMPLATES   | X       | X         |      | X          |       |            |
| VIDEOS      | X       | X*        |      | X          |       |            |

Note that on macOS/iOS, the Videos folder is called "Movies".

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_GetUserFolder](SDL_GetUserFolder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryFilesystem](CategoryFilesystem)

