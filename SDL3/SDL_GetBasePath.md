###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetBasePath

Get the directory where the application was run from.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
const char * SDL_GetBasePath(void);
```

## Return Value

(const char *) Returns an absolute path in UTF-8 encoding to the
application data directory. NULL will be returned on error or when the
platform doesn't implement this functionality, call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL caches the result of this call internally, but the first call to this
function is not necessarily fast, so plan accordingly.

**macOS and iOS Specific Functionality**: If the application is in a ".app"
bundle, this function returns the Resource directory (e.g.
MyApp.app/Contents/Resources/). This behaviour can be overridden by adding
a property to the Info.plist file. Adding a string key with the name
[SDL_FILESYSTEM_BASE_DIR_TYPE](SDL_FILESYSTEM_BASE_DIR_TYPE) with a
supported value will change the behaviour.

Supported values for the
[SDL_FILESYSTEM_BASE_DIR_TYPE](SDL_FILESYSTEM_BASE_DIR_TYPE) property
(Given an application in /Applications/SDLApp/MyApp.app):

- `resource`: bundle resource directory (the default). For example:
  `/Applications/SDLApp/MyApp.app/Contents/Resources`
- `bundle`: the Bundle directory. For example:
  `/Applications/SDLApp/MyApp.app/`
- `parent`: the containing directory of the bundle. For example:
  `/Applications/SDLApp/`

**Nintendo 3DS Specific Functionality**: This function returns "romfs"
directory of the application as it is uncommon to store resources outside
the executable. As such it is not a writable directory.

The returned path is guaranteed to end with a path separator ('\\' on
Windows, '/' on most other platforms).

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetPrefPath](SDL_GetPrefPath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

