###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetBasePath

Get the directory where the application was run from.

## Syntax

```c
char* SDL_GetBasePath(void);

```

## Return Value

Returns an absolute path in UTF-8 encoding to the application data
directory. NULL will be returned on error or when the platform doesn't
implement this functionality, call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This is not necessarily a fast call, so you should call this once near
startup and save the string if you need it.

**Mac OS X and iOS Specific Functionality**: If the application is in a
".app" bundle, this function returns the Resource directory (e.g.
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

The returned path is guaranteed to end with a path separator ('\' on
Windows, '/' on most other platforms).

The pointer returned is owned by the caller. Please call
[SDL_free](SDL_free)() on the pointer when done with it.

## Version

This function is available since SDL 2.0.1.

## Related Functions

* [SDL_GetPrefPath](SDL_GetPrefPath)

----
[CategoryAPI](CategoryAPI)

