###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowWMInfo

Get driver-specific information about a window.

## Syntax

```c
int SDL_GetWindowWMInfo(SDL_Window *window, SDL_SysWMinfo *info, Uint32 version);

```

## Function Parameters

|                 |                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| **window**      | the window about which information is being requested                                                 |
| **info**        | an [SDL_SysWMinfo](SDL_SysWMinfo) structure filled in with window information                         |
| **version**     | the version of info being requested, should be [SDL_SYSWM_CURRENT_VERSION](SDL_SYSWM_CURRENT_VERSION) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You must include [SDL_syswm](SDL_syswm).h for the declaration of
[SDL_SysWMinfo](SDL_SysWMinfo).

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"
#include "SDL_syswm.h"

int main(int argc, char *argv[]) {
  SDL_Window* window;
  SDL_SysWMinfo info;

  SDL_Init(0);

  window = SDL_CreateWindow("", 0, 0, 0, 0, SDL_WINDOW_HIDDEN);

  SDL_VERSION(&info.version); /* initialize info structure with SDL version info */

  if(SDL_GetWindowWMInfo(window,&info) == 0) { /* the call returns 0 on success */
    /* success */
    const char *subsystem = "an unknown system!";
    switch(info.subsystem) {
      case SDL_SYSWM_UNKNOWN:   break;
      case SDL_SYSWM_WINDOWS:   subsystem = "Microsoft Windows(TM)";  break;
      case SDL_SYSWM_X11:       subsystem = "X Window System";        break;
#if SDL_VERSION_ATLEAST(2, 0, 3)
      case SDL_SYSWM_WINRT:     subsystem = "WinRT";                  break;
#endif
      case SDL_SYSWM_DIRECTFB:  subsystem = "DirectFB";               break;
      case SDL_SYSWM_COCOA:     subsystem = "Apple OS X";             break;
      case SDL_SYSWM_UIKIT:     subsystem = "UIKit";                  break;
#if SDL_VERSION_ATLEAST(2, 0, 2)
      case SDL_SYSWM_WAYLAND:   subsystem = "Wayland";                break;
      case SDL_SYSWM_MIR:       subsystem = "Mir";                    break;
#endif
#if SDL_VERSION_ATLEAST(2, 0, 4)
      case SDL_SYSWM_ANDROID:   subsystem = "Android";                break;
#endif
#if SDL_VERSION_ATLEAST(2, 0, 5)
      case SDL_SYSWM_VIVANTE:   subsystem = "Vivante";                break;
#endif
    }

    SDL_Log("This program is running SDL version %d.%d.%d on %s",
        (int)info.version.major,
        (int)info.version.minor,
        (int)info.version.patch,
        subsystem);
  } else {
    /* call failed */
    SDL_LogError(SDL_LOG_CATEGORY_ERROR, "Couldn't get window information: %s", SDL_GetError());
  }

  SDL_DestroyWindow(window);
  SDL_Quit();

  return 0;
}

```

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo), [CategorySWM](CategorySWM)

<!-- #Actually from SDL_syswm.h header but listed in both categories for the wiki. -->


