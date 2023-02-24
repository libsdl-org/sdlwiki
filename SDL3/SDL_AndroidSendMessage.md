###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AndroidSendMessage

Send a user command to SDLActivity.

## Syntax

```c
int SDL_AndroidSendMessage(Uint32 command, int param);

```

## Function Parameters

|                 |                                                      |
| --------------- | ---------------------------------------------------- |
| **command**     | user command that must be greater or equal to 0x8000 |
| **param**       | user parameter                                       |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Override "boolean onUnhandledMessage(Message msg)" to handle the message.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAndroid](CategoryAndroid)


