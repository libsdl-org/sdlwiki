###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogOutputFunction

The prototype for the log output callback function.

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
typedef void (SDLCALL *SDL_LogOutputFunction)(void *userdata, int category, SDL_LogPriority priority, const char *message);
```

## Function Parameters

|                  |                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------- |
| **userdata**     | what was passed as `userdata` to [SDL_LogSetOutputFunction](SDL_LogSetOutputFunction)() |
| **category**     | the category of the message                                                             |
| **priority**     | the priority of the message                                                             |
| **message**      | the message being output                                                                |

## Remarks

This function is called by SDL when there is new text to be logged.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryLog](CategoryLog)

