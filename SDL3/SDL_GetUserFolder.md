###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetUserFolder

Finds the most suitable user folder for @p purpose, and returns its path in OS-specific notation.

## Syntax

```c
char* SDL_GetUserFolder(SDL_Folder folder);

```

## Function Parameters

|                |                            |
| -------------- | -------------------------- |
| **folder**     | The type of folder to find |

## Return Value

Returns Either a null-terminated C string containing the full path to the
folder, or NULL if an error happened.

## Remarks

Many OSes provide certain standard folders for certain purposes, such as
storing pictures, music or videos for a certain user. This function gives
the path for many of those special locations.

This function is specifically for _user_ folders, which are meant for the
user to access and manage. For application-specific folders, meant to hold
data for the application to manage, see
[SDL_GetBasePath](SDL_GetBasePath)() and
[SDL_GetPrefPath](SDL_GetPrefPath)().

Note that the function is expensive, and should be called once at the
beginning of the execution and kept for as long as needed.

The returned value is owned by the caller and should be freed with
[SDL_free](SDL_free)().

If NULL is returned, the error may be obtained with
[SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_Folder](SDL_Folder)

----
[CategoryAPI](CategoryAPI)

