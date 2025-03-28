# SDL_GetErrorMsg

Get the last error message that was set for the current thread.

## Header File

Defined in [SDL_error.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_error.h)

## Syntax

```c
char * SDL_GetErrorMsg(char *errstr, int maxlen);
```

## Function Parameters

|        |            |                                                                                   |
| ------ | ---------- | --------------------------------------------------------------------------------- |
| char * | **errstr** | A buffer to fill with the last error message that was set for the current thread. |
| int    | **maxlen** | The size of the buffer pointed to by the errstr parameter.                        |

## Return Value

(char *) Returns the pointer passed in as the `errstr` parameter.

## Remarks

This allows the caller to copy the error string into a provided buffer, but
otherwise operates exactly the same as [SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 2.0.14.

## See Also

- [SDL_GetError](SDL_GetError)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

