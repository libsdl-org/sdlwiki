###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Load

Set the text of an RTF context, with data loaded from a filename.

## Syntax

```c
int RTF_Load(RTF_Context *ctx, const char *file);

```

## Function Parameters

|              |                                      |
| ------------ | ------------------------------------ |
| **ctx**      | the RTF context to update.           |
| **file**     | the file path to load RTF data from. |

## Return Value

Returns 0 on success, -1 on failure.

## Remarks

This can be called multiple times to change the text displayed.

On failure, call [RTF_GetError](RTF_GetError)() to get a human-readable
text message corresponding to the error.

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI)

