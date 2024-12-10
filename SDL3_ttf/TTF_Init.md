###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_Init

Initialize SDL_ttf.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_Init(void);
```

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

You must successfully call this function before it is safe to call any
other function in this library.

It is safe to call this more than once, and each successful
[TTF_Init](TTF_Init)() call should be paired with a matching
[TTF_Quit](TTF_Quit)() call.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_Quit](TTF_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

