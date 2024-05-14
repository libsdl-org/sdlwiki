###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WinRT_Path

WinRT / Windows Phone path types

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef enum SDL_WinRT_Path
{
    /** The installed app's root directory.
        Files here are likely to be read-only. */
    SDL_WINRT_PATH_INSTALLED_LOCATION,

    /** The app's local data store.  Files may be written here */
    SDL_WINRT_PATH_LOCAL_FOLDER,

    /** The app's roaming data store.  Unsupported on Windows Phone.
        Files written here may be copied to other machines via a network
        connection.
    */
    SDL_WINRT_PATH_ROAMING_FOLDER,

    /** The app's temporary data store.  Unsupported on Windows Phone.
        Files written here may be deleted at any time. */
    SDL_WINRT_PATH_TEMP_FOLDER
} SDL_WinRT_Path;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySystem](CategorySystem)

