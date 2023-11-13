###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateWindowFrom

Create an SDL window from properties representing an existing native window.

## Syntax

```c
SDL_Window* SDL_CreateWindowFrom(SDL_PropertiesID props);

```

## Function Parameters

|               |                                                              |
| ------------- | ------------------------------------------------------------ |
| **props**     | a set of properties describing the native window and options |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

On macOS:

```
"cocoa.window" (pointer) - the (__unsafe_unretained) NSWindow associated with the window
"cocoa.view" (pointer) - optional, the (__unsafe_unretained) NSView associated with the window, defaults to [window contentView]
```

On Windows:

```
"win32.hwnd" (pointer) - the HWND associated with the window
"win32.pixel_format_hwnd" (pointer) - optional, another window to share pixel format with, useful for OpenGL windows
```

On X11:

```
"x11.window" (number) - the X11 Window associated with the window
```

On all platforms:

```
"opengl" (boolean) - optional, true if the window will be used with OpenGL rendering
"vulkan" (boolean) - optional, true if the window will be used with Vulkan rendering
```

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


