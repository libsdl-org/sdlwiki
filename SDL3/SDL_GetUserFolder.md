###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetUserFolder

Finds the most suitable user folder for a specific purpose.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
const char * SDL_GetUserFolder(SDL_Folder folder);
```

## Function Parameters

|                          |            |                             |
| ------------------------ | ---------- | --------------------------- |
| [SDL_Folder](SDL_Folder) | **folder** | the type of folder to find. |

## Return Value

(const char *) Returns either a null-terminated C string containing the
full path to the folder, or NULL if an error happened.

## Remarks

Many OSes provide certain standard folders for certain purposes, such as
storing pictures, music or videos for a certain user. This function gives
the path for many of those special locations.

This function is specifically for _user_ folders, which are meant for the
user to access and manage. For application-specific folders, meant to hold
data for the application to manage, see
[SDL_GetBasePath](SDL_GetBasePath)() and
[SDL_GetPrefPath](SDL_GetPrefPath)().

The returned path is guaranteed to end with a path separator ('\\' on
Windows, '/' on most other platforms).

If NULL is returned, the error may be obtained with
[SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

