# SDL_AndroidSendMessage

Send a user command to SDLActivity.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
int SDL_AndroidSendMessage(Uint32 command, int param);
```

## Function Parameters

|                  |             |                                                       |
| ---------------- | ----------- | ----------------------------------------------------- |
| [Uint32](Uint32) | **command** | user command that must be greater or equal to 0x8000. |
| int              | **param**   | user parameter.                                       |

## Return Value

(int) Returns 0 on success, otherwise -1.

## Remarks

Override "boolean onUnhandledMessage(Message msg)" to handle the message.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

