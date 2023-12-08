###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWFromFile

Use this function to create a new [SDL_RWops](SDL_RWops.md) structure for reading from and/or writing to a named file.

## Syntax

```c
SDL_RWops* SDL_RWFromFile(const char *file,
                          const char *mode);

```

## Function Parameters

|              |                                                                        |
| ------------ | ---------------------------------------------------------------------- |
| **file**     | a UTF-8 string representing the filename to open                       |
| **mode**     | an ASCII string representing the mode to be used for opening the file. |

## Return Value

Returns a pointer to the [SDL_RWops](SDL_RWops.md) structure that is created,
or NULL on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

The `mode` string is treated roughly the same as in a call to the C
library's fopen(), even if SDL doesn't happen to use fopen() behind the
scenes.

Available `mode` strings:

- "r": Open a file for reading. The file must exist.
- "w": Create an empty file for writing. If a file with the same name
  already exists its content is erased and the file is treated as a new
  empty file.
- "a": Append to a file. Writing operations append data at the end of the
  file. The file is created if it does not exist.
- "r+": Open a file for update both reading and writing. The file must
  exist.
- "w+": Create an empty file for both reading and writing. If a file with
  the same name already exists its content is erased and the file is
  treated as a new empty file.
- "a+": Open a file for reading and appending. All writing operations are
  performed at the end of the file, protecting the previous content to be
  overwritten. You can reposition (fseek, rewind) the internal pointer to
  anywhere in the file for reading, but writing operations will move it
  back to the end of file. The file is created if it does not exist.

**NOTE**: In order to open a file as a binary file, a "b" character has to
be included in the `mode` string. This additional "b" character can either
be appended at the end of the string (thus making the following compound
modes: "rb", "wb", "ab", "r+b", "w+b", "a+b") or be inserted between the
letter and the "+" sign for the mixed modes ("rb+", "wb+", "ab+").
Additional characters may follow the sequence, although they should have no
effect. For example, "t" is sometimes appended to make explicit the file is
a text file.

This function supports Unicode filenames, but they must be encoded in UTF-8
format, regardless of the underlying operating system.

As a fallback, [SDL_RWFromFile](SDL_RWFromFile.md)() will transparently open a
matching filename in an Android app's `assets`.

Closing the [SDL_RWops](SDL_RWops.md) will close the file handle SDL is
holding internally.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFP](SDL_RWFromFP.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWtell](SDL_RWtell.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md)
