###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_Init

Initialize SDL_ttf.

## Syntax

```c
int TTF_Init(void);

```

## Return Value

Returns 0 on success, -1 on error.

## Remarks

You must successfully call this function before it is safe to call any
other function in this library, with one exception: a human-readable error
message can be retrieved from [TTF_GetError](TTF_GetError)() if this
function fails.

SDL must be initialized before calls to functions in this library, because
this library uses utility functions from the SDL library.

It is safe to call this more than once; the library keeps a counter of init
calls, and decrements it on each call to [TTF_Quit](TTF_Quit), so you must
pair your init and quit calls.

## Version

This function is available since SDL_ttf 2.0.12.

## Related Functions

* [TTF_Quit](TTF_Quit)

----
[CategoryAPI](CategoryAPI)

