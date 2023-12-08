###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetScript

Set a global script to be used for text shaping.

## Deprecated

This function expects an hb_script_t value, from HarfBuzz, cast to an int,
and affects all fonts globally. Please use
[TTF_SetFontScriptName](TTF_SetFontScriptName.md)() instead, which accepts a
string that is converted to an equivalent int internally, and operates on a
per-font basis.

This is a global setting; fonts will favor a value set with
[TTF_SetFontScriptName](TTF_SetFontScriptName.md)(), but if they have not had
one explicitly set, they will use the value specified here.

The default value is `HB_SCRIPT_UNKNOWN`.

## Syntax

```c
int TTF_SetScript(int script); /* hb_script_t */

```

## Return Value

Returns 0, or -1 if SDL_ttf is not compiled with HarfBuzz support.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_SetFontScriptName](TTF_SetFontScriptName.md)

----
[CategoryAPI](CategoryAPI.md)
