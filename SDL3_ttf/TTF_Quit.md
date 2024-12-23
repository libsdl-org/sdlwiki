###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_Quit

Deinitialize SDL_ttf.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_Quit(void);
```

## Remarks

You must call this when done with the library, to free internal resources.
It is safe to call this when the library isn't initialized, as it will just
return immediately.

Once you have as many quit calls as you have had successful calls to
[TTF_Init](TTF_Init), the library will actually deinitialize.

Please note that this does not automatically close any fonts that are still
open at the time of deinitialization, and it is possibly not safe to close
them afterwards, as parts of the library will no longer be initialized to
deal with it. A well-written program should call
[TTF_CloseFont](TTF_CloseFont)() on any open fonts before calling this
function!

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

