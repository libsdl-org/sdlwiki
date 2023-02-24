###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFreeTypeVersion

Query the version of the FreeType library in use.

## Syntax

```c
void TTF_GetFreeTypeVersion(int *major, int *minor, int *patch);

```

## Function Parameters

|               |                                                             |
| ------------- | ----------------------------------------------------------- |
| **major**     | to be filled in with the major version number. Can be NULL. |
| **minor**     | to be filled in with the minor version number. Can be NULL. |
| **patch**     | to be filled in with the param version number. Can be NULL. |

## Remarks

[TTF_Init](TTF_Init)() should be called before calling this function.

## Version

This function is available since SDL_ttf 2.0.18.

## Related Functions

* [TTF_Init](TTF_Init)

----
[CategoryAPI](CategoryAPI)

