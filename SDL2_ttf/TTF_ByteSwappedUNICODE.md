###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_ByteSwappedUNICODE

Tell SDL_ttf whether UNICODE text is generally byteswapped.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
void TTF_ByteSwappedUNICODE(SDL_bool swapped);
```

## Function Parameters

|          |             |                                                  |
| -------- | ----------- | ------------------------------------------------ |
| SDL_bool | **swapped** | boolean to indicate whether text is byteswapped. |

## Remarks

A UNICODE BOM character in a string will override this setting for the
remainder of that string.

## Version

This function is available since SDL_ttf 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

