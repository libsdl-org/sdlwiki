###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_ByteSwappedUNICODE

Tell SDL_ttf whether UNICODE text is generally byteswapped.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
void TTF_ByteSwappedUNICODE(bool swapped);
```

## Function Parameters

|      |             |                                                  |
| ---- | ----------- | ------------------------------------------------ |
| bool | **swapped** | boolean to indicate whether text is byteswapped. |

## Remarks

A UNICODE BOM character in a string will override this setting for the
remainder of that string.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

