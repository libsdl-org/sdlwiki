###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetScript

Set a global script to be used for text shaping.

## Deprecated

This function expects an hb_script_t value, from HarfBuzz, cast to an int,
and affects all fonts globally. Please use
[TTF_SetFontScriptName](TTF_SetFontScriptName)() instead, which accepts a
string that is converted to an equivalent int internally, and operates on a
per-font basis.

This is a global setting; fonts will favor a value set with
[TTF_SetFontScriptName](TTF_SetFontScriptName)(), but if they have not had
one explicitly set, they will use the value specified here.

The default value is `HB_SCRIPT_UNKNOWN`.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
int TTF_SetScript(int script); /* hb_script_t */
```

## Return Value

(int) Returns 0, or -1 if SDL_ttf is not compiled with HarfBuzz support.

## Version

This function is available since SDL_ttf 2.0.18.

## See Also

- [TTF_SetFontScriptName](TTF_SetFontScriptName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

