###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPrefPath

Get the user-and-app-specific path where files can be written.

## Header File

Defined in [SDL_filesystem.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_filesystem.h)

## Syntax

```c
char* SDL_GetPrefPath(const char *org, const char *app);
```

## Function Parameters

|              |         |                               |
| ------------ | ------- | ----------------------------- |
| const char * | **org** | the name of your organization |
| const char * | **app** | the name of your application  |

## Return Value

(char *) Returns a UTF-8 string of the user directory in platform-dependent
notation. NULL if there's a problem (creating directory failed, etc.).

## Remarks

Get the "pref dir". This is meant to be where users can write personal
files (preferences and save games, etc) that are specific to your
application. This directory is unique per user, per application.

This function will decide the appropriate location in the native
filesystem, create the directory if necessary, and return a string of the
absolute path to the directory in UTF-8 encoding.

On Windows, the string might look like:

`C:\\Users\\bob\\AppData\\Roaming\\My Company\\My Program Name\\`

On Linux, the string might look like:

`/home/bob/.local/share/My Program Name/`

On Mac OS X, the string might look like:

`/Users/bob/Library/Application Support/My Program Name/`

You should assume the path returned by this function is the only safe place
to write files (and that [SDL_GetBasePath](SDL_GetBasePath)(), while it
might be writable, or even the parent of the returned path, isn't where you
should be writing things).

Both the org and app strings may become part of a directory name, so please
follow these rules:

- Try to use the same org string (_including case-sensitivity_) for all
  your applications that use this function.
- Always use a unique app string for each one, and make sure it never
  changes for an app once you've decided on it.
- Unicode characters are legal, as long as it's UTF-8 encoded, but...
- ...only use letters, numbers, and spaces. Avoid punctuation like "Game
  Name 2: Bad Guy's Revenge!" ... "Game Name 2" is sufficient.

The returned path is guaranteed to end with a path separator ('\\' on
Windows, '/' on most other platforms).

The pointer returned is owned by the caller. Please call
[SDL_free](SDL_free)() on the pointer when done with it.

## Version

This function is available since SDL 2.0.1.

## See Also

- [SDL_GetBasePath](SDL_GetBasePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

