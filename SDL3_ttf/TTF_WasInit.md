###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_WasInit

Check if SDL_ttf is initialized.

## Syntax

```c
int TTF_WasInit(void);

```

## Return Value

Returns the current number of initialization calls, that need to eventually
be paired with this many calls to [TTF_Quit](TTF_Quit.md)().

## Remarks

This reports the number of times the library has been initialized by a call
to [TTF_Init](TTF_Init.md)(), without a paired deinitialization request from
[TTF_Quit](TTF_Quit.md)().

In short: if it's greater than zero, the library is currently initialized
and ready to work. If zero, it is not initialized.

Despite the return value being a signed integer, this function should not
return a negative number.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_Init](TTF_Init.md)
* [TTF_Quit](TTF_Quit.md)

----
[CategoryAPI](CategoryAPI.md)
