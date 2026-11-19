# SDL_GetCachePath

Get the user-and-app-specific path where cache files can be written.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
char * SDL_GetCachePath(const char *org, const char *app);
```

## Function Parameters

|              |         |                                |
| ------------ | ------- | ------------------------------ |
| const char * | **org** | the name of your organization. |
| const char * | **app** | the name of your application.  |

## Return Value

(char *) Returns a UTF-8 string of the user's cache directory in
platform-dependent notation. NULL if there's a problem (creating directory
failed, etc.). This should be freed with [SDL_free](SDL_free)() when it is
no longer needed. Returns NULL if platform has no separate cache directory,
but this isn't strictly speaking an error.

## Remarks

Some platforms offer a designated space on the filesystem for cached data
(data downloaded or calculated and saved to local files to avoid the
expense of obtaining it again, but can be reproduced if lost).

It's possible that the system will know not to back up these specific files
and/or it will know to clear these files out from time to time. If
available, it might be useful to take advantage of this directory instead
of storing everything in one place.

This function will decide the appropriate location in the native
filesystem, create the directory if necessary, and return a string of the
absolute path to the directory in UTF-8 encoding.

On Windows, the string might look like:

`C:\\Users\\bob\\AppData\\Local\\My Company\\My Program Name\\`

On Linux, the string might look like:

`/home/bob/.cache/My Program Name/`

On macOS, the string might look like:

`/Users/bob/Library/Cache/My Program Name/`

This function may return NULL if there is no designated cache directory for
a given platform. Best practices in this case is not to treat this as a
fatal error, but instead fall back to [SDL_GetPrefPath](SDL_GetPrefPath)()
as a safe place to write files generically, and write cache files somewhere
under that path.

Both the org and app strings may become part of a directory name, so please
follow these rules:

- Use the same strings you would pass to
  [SDL_GetPrefPath](SDL_GetPrefPath)!
- Try to use the same org string (_including case-sensitivity_) for all
  your applications that use this function.
- Always use a unique app string for each one, and make sure it never
  changes for an app once you've decided on it.
- Unicode characters are legal, as long as they are UTF-8 encoded, but...
- ...only use letters, numbers, and spaces. Avoid punctuation like "Game
  Name 2: Bad Guy's Revenge!" ... "Game Name 2" is sufficient.

Unlike [SDL_GetPrefPath](SDL_GetPrefPath)(), where historical mistakes were
made, `org` is _not_ allowed to be NULL or "". New apps should specify
proper strings here (even if they need to fall back to NULL or "" for
[SDL_GetPrefPath](SDL_GetPrefPath)() to keep existing app installations
working without disruption).

The returned path is guaranteed to end with a path separator ('\\' on
Windows, '/' on most other platforms).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GetPrefPath](SDL_GetPrefPath)
- [SDL_GetBasePath](SDL_GetBasePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

