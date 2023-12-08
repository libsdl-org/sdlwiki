###### (This function is part of SDL_rtf, a separate library from SDL.)
# RTF_Linked_Version

Query the version of SDL_rtf that the program is linked against.

## Syntax

```c
const SDL_version * RTF_Linked_Version(void);

```

## Return Value

Returns a pointer to the version information.

## Remarks

This function gets the version of the dynamically linked SDL_rtf library.
This is separate from the SDL_RTF_VERSION() macro, which tells you what
version of the SDL_rtf headers you compiled against.

This returns static internal data; do not free or modify it!

## Version

This function is available since SDL_rtf 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
