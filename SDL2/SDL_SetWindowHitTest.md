###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowHitTest

Provide a callback that decides if a window region has special properties.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetWindowHitTest(SDL_Window * window,
                         SDL_HitTest callback,
                         void *callback_data);

```

## Function Parameters

|                       |                                                    |
| --------------------- | -------------------------------------------------- |
| **window**            | the window to set hit-testing on                   |
| **callback**          | the function to call when doing a hit-test         |
| **callback_data**     | an app-defined void pointer passed to **callback** |

## Return Value

Returns 0 on success or -1 on error (including unsupported); call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Normally windows are dragged and resized by decorations provided by the
system window manager (a title bar, borders, etc), but for some apps, it
makes sense to drag them from somewhere else inside the window itself; for
example, one might have a borderless window that wants to be draggable from
any part, or simulate its own title bar, etc.

This function lets the app provide a callback that designates pieces of a
given window as special. This callback is run during event processing if we
need to tell the OS to treat a region of the window specially; the use of
this callback is known as "hit testing."

Mouse input may not be delivered to your application if it is within a
special area; the OS will often apply that input to moving the window or
resizing the window and not deliver it to the application.

Specifying NULL for a callback disables hit-testing. Hit-testing is
disabled by default.

Platforms that don't support this functionality will return -1
unconditionally, even if you're attempting to disable hit-testing.

Your callback may fire at any time, and its firing does not indicate any
specific behavior (for example, on Windows, this certainly might fire when
the OS is deciding whether to drag your window, but it fires for lots of
other reasons, too, some unrelated to anything you probably care about _and
when the mouse isn't actually at the location it is testing_). Since this
can fire at any time, you should try to keep your callback efficient,
devoid of allocations, etc.

## Version

This function is available since SDL 2.0.4.

----
[CategoryAPI](CategoryAPI)

