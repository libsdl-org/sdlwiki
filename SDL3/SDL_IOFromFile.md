###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IOFromFile

Use this function to create a new [SDL_IOStream](SDL_IOStream) structure for reading from and/or writing to a named file.

## Syntax

```c
SDL_IOStream* SDL_IOFromFile(const char *file, const char *mode);

```

## Function Parameters

|              |                                                                        |
| ------------ | ---------------------------------------------------------------------- |
| **file**     | a UTF-8 string representing the filename to open                       |
| **mode**     | an ASCII string representing the mode to be used for opening the file. |

## Return Value

Returns a pointer to the [SDL_IOStream](SDL_IOStream) structure that is
created, or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
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

As a fallback, [SDL_IOFromFile](SDL_IOFromFile)() will transparently open a
matching filename in an Android app's `assets`.

Closing the [SDL_IOStream](SDL_IOStream) will close SDL's internal file
handle.

The following properties may be set at creation time by SDL:

- [`SDL_PROP_IOSTREAM_WINDOWS_HANDLE_POINTER`](SDL_PROP_IOSTREAM_WINDOWS_HANDLE_POINTER):
  a pointer, that can be cast to a win32 `HANDLE`, that this
  [SDL_IOStream](SDL_IOStream) is using to access the filesystem. If the
  program isn't running on Windows, or SDL used some other method to access
  the filesystem, this property will not be set.
- [`SDL_PROP_IOSTREAM_STDIO_HANDLE_POINTER`](SDL_PROP_IOSTREAM_STDIO_HANDLE_POINTER):
  a pointer, that can be cast to a stdio `FILE *`, that this
  [SDL_IOStream](SDL_IOStream) is using to access the filesystem. If SDL
  used some other method to access the filesystem, this property will not
  be set. PLEASE NOTE that if SDL is using a different C runtime than your
  app, trying to use this pointer will almost certainly result in a crash!
  This is mostly a problem on Windows; make sure you build SDL and your app
  with the same compiler and settings to avoid it.
- [`SDL_PROP_IOSTREAM_ANDROID_AASSET_POINTER`](SDL_PROP_IOSTREAM_ANDROID_AASSET_POINTER):
  a pointer, that can be cast to an Android NDK `AAsset *`, that this
  [SDL_IOStream](SDL_IOStream) is using to access the filesystem. If SDL
  used some other method to access the filesystem, this property will not
  be set.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_IOFromConstMem](SDL_IOFromConstMem)
* [SDL_IOFromMem](SDL_IOFromMem)
* [SDL_CloseIO](SDL_CloseIO)
* [SDL_ReadIO](SDL_ReadIO)
* [SDL_SeekIO](SDL_SeekIO)
* [SDL_TellIO](SDL_TellIO)
* [SDL_WriteIO](SDL_WriteIO)

----
[CategoryAPI](CategoryAPI)

