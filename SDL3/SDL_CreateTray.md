# SDL_CreateTray

Create an icon to be placed in the operating system's tray, or equivalent.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_Tray * SDL_CreateTray(SDL_Surface *icon, const char *tooltip);
```

## Function Parameters

|                              |             |                                                                                                                          |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **icon**    | a surface to be used as icon. May be NULL.                                                                               |
| const char *                 | **tooltip** | a tooltip to be displayed when the mouse hovers the icon in UTF-8 encoding. Not supported on all platforms. May be NULL. |

## Return Value

([SDL_Tray](SDL_Tray) *) Returns The newly created system tray icon.

## Remarks

Many platforms advise not using a system tray unless persistence is a
necessary feature. Avoid needlessly creating a tray icon, as the user may
feel like it clutters their interface.

Using tray icons require the video subsystem.

## Thread Safety

This function should only be called on the main thread.

## Code Examples

A simple program that creates a system tray with a single button that quits the
program:

```c
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

void callback_quit(void *userdata, SDL_TrayEntry *invoker)
{
    SDL_Event e;
    e.type = SDL_EVENT_QUIT;
    SDL_PushEvent(&e);
}

int main(int argc, char *argv[])
{
    SDL_Tray *tray;
    SDL_TrayMenu *menu;
    SDL_TrayEntry *entry;
    SDL_Event e;

    SDL_Init(SDL_INIT_VIDEO);

    // Create the entry in the system tray. A regular app will want to provide
    // an SDL_Surface instead of NULL.
    tray = SDL_CreateTray(NULL, "My tray");

    // Create a context menu for the tray.
    menu = SDL_CreateTrayMenu(tray);

    // Create a button in the comtext menu.
    entry = SDL_InsertTrayEntryAt(menu, -1, "Quit", SDL_TRAYENTRY_BUTTON);

    // Set the callback for the button
    SDL_SetTrayEntryCallback(entry, callback_quit, NULL);

    // Run the main loop...
    while (SDL_WaitEvent(&e)) {
        if (e.type == SDL_EVENT_QUIT) {
            break;
        }
    }

    // No need to destroy anything other than the tray itself - the rest is
    // destroyed automatically.
    SDL_DestroyTray(tray);

    SDL_Quit();

    return 0;
}
```

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTrayMenu](SDL_CreateTrayMenu)
- [SDL_GetTrayMenu](SDL_GetTrayMenu)
- [SDL_DestroyTray](SDL_DestroyTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

