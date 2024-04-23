###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidSendMessage

Send a user command to SDLActivity.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
int SDL_AndroidSendMessage(Uint32 command, int param);

```

## Function Parameters

|                 |                                                      |
| --------------- | ---------------------------------------------------- |
| **command**     | user command that must be greater or equal to 0x8000 |
| **param**       | user parameter                                       |

## Remarks

Override "boolean onUnhandledMessage(Message msg)" to handle the message.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

