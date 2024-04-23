###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DropEvent

An event used to request a file open by the system (event.drop.*) This event is enabled by default, you can disable it with [SDL_EventState](SDL_EventState)().

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_DropEvent
{
    Uint32 type;        /**< ::SDL_DROPBEGIN or ::SDL_DROPFILE or ::SDL_DROPTEXT or ::SDL_DROPCOMPLETE */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    char *file;         /**< The file name, which should be freed with SDL_free(), is NULL on begin/complete */
    Uint32 windowID;    /**< The window that was dropped on, if any */
} SDL_DropEvent;
```

## Code Examples

```c++
// Example program:
// SDL_DropEvent usage

#include "SDL.h"

int main(int argc, char *argv[]) {
    SDL_bool done;
    SDL_Window *window;
    SDL_Event event;                        // Declare event handle
    char* dropped_filedir;                  // Pointer for directory of dropped file

    SDL_Init(SDL_INIT_VIDEO);               // SDL2 initialization

    window = SDL_CreateWindow(  // Create a window
        "SDL_DropEvent usage, please drop the file on window",
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        640,
        480,
        SDL_WINDOW_OPENGL
    );

    // Check that the window was successfully made
    if (window == NULL) {
        // In the event that the window could not be made...
        SDL_Log("Could not create window: %s", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    SDL_EventState(SDL_DROPFILE, SDL_ENABLE);

    done = SDL_FALSE;
    while (!done) {                         // Program loop
        while (!done && SDL_PollEvent(&event)) {
            switch (event.type) {
                case (SDL_QUIT): {          // In case of exit
                    done = SDL_TRUE;
                    break;
                }

                case (SDL_DROPFILE): {      // In case if dropped file
                    dropped_filedir = event.drop.file;
                    // Shows directory of dropped file
                    SDL_ShowSimpleMessageBox(
                        SDL_MESSAGEBOX_INFORMATION,
                        "File dropped on window",
                        dropped_filedir,
                        window
                    );
                    SDL_free(dropped_filedir);    // Free dropped_filedir memory
                    break;
               }
            }
        }
        SDL_Delay(0);
    }

    SDL_DestroyWindow(window);        // Close and destroy the window

    SDL_Quit();                       // Clean up
    return 0;
}
```

## Data Fields

|        |                 |                                                                                 |
| ------ | --------------- | ------------------------------------------------------------------------------- |
| Uint32 | '''type'''      | the event type; SDL_DROPFILE, SDL_DROPTEXT, SDL_DROPBEGIN, or SDL_DROPCOMPLETE  |
| Uint32 | '''timestamp''' | timestamp of the event                                                          |
| char*  | '''file'''      | the file name, which should be freed with SDL_free(), is NULL on BEGIN/COMPLETE |
| Uint32 | '''windowID'''  | the window that was dropped on, if any                                          |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_Event](SDL_Event)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


