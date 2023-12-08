###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WinRTGetFSPathUNICODE

Retrieve a WinRT defined path on the local file system.

## Syntax

```c
const wchar_t * SDL_WinRTGetFSPathUNICODE(SDL_WinRT_Path pathType);

```

## Function Parameters

|                  |                                                                       |
| ---------------- | --------------------------------------------------------------------- |
| **pathType**     | the type of path to retrieve, one of [SDL_WinRT_Path](SDL_WinRT_Path.md) |

## Return Value

Returns a UCS-2 string (16-bit, wide-char) containing the path, or NULL if
the path is not available for any reason; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Not all paths are available on all versions of Windows. This is especially
true on Windows Phone. Check the documentation for the given
[SDL_WinRT_Path](SDL_WinRT_Path.md) for more information on which path types
are supported where.

Documentation on most app-specific path types on WinRT can be found on
MSDN, at the URL:

https://msdn.microsoft.com/en-us/library/windows/apps/hh464917.aspx

## Version

This function is available since SDL 2.0.3.

## Related Functions

* [SDL_WinRTGetFSPathUTF8](SDL_WinRTGetFSPathUTF8.md)

----
[CategoryAPI](CategoryAPI.md)
