###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ReportAssertion

Never call this directly.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
SDL_AssertState SDL_ReportAssertion(SDL_AssertData *data,
                                const char *func,
                                const char *file, int line);
```

## Function Parameters

|                                    |          |                        |
| ---------------------------------- | -------- | ---------------------- |
| [SDL_AssertData](SDL_AssertData) * | **data** | assert data structure. |
| const char *                       | **func** | function name.         |
| const char *                       | **file** | file name.             |
| int                                | **line** | line number.           |

## Return Value

([SDL_AssertState](SDL_AssertState)) Returns assert state.

## Remarks

Use the [SDL_assert](SDL_assert) macros instead.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAssert](CategoryAssert)

