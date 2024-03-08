###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWread

Read from a data source.

## Syntax

```c
size_t SDL_RWread(SDL_RWops *context, void *ptr, size_t size);

```

## Function Parameters

|                 |                                                   |
| --------------- | ------------------------------------------------- |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure  |
| **ptr**         | a pointer to a buffer to read data into           |
| **size**        | the number of bytes to read from the data source. |

## Return Value

Returns the number of bytes read, or 0 on end of file or other error.

## Remarks

This function reads up `size` bytes from the data source to the area
pointed at by `ptr`. This function may read less bytes than requested. It
will return zero when the data stream is completely read, or -1 on error.
For streams that support non-blocking operation, if nothing was read
because it would require blocking, this function returns -2 to distinguish
that this is not an error or end-of-file, and the caller can try again
later.

[SDL_RWread](SDL_RWread)() is actually a function wrapper that calls the
[SDL_RWops](SDL_RWops)'s `read` method appropriately, to simplify
application development.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_RWops *rw = SDL_RWFromFile("test.bin","r");
if (rw != NULL) {
    extern Uint8 buf[256];
    SDL_RWread(rw, buf, sizeof (buf), 1);
    SDL_RWclose(rw);
}
```

Read a complete file in memory (assuming size can be detected) (from [OpenGL WikiBook](https://gitlab.com/wikibooks-opengl/modern-tutorials/blob/master/common-sdl2/shader_utils.cpp)):
```c++
char* file_read(const char* filename) {
	SDL_RWops *rw = SDL_RWFromFile(filename, "rb");
	if (rw == NULL) return NULL;

	Sint64 res_size = SDL_RWsize(rw);
	char* res = (char*)malloc(res_size + 1);

	Sint64 nb_read_total = 0, nb_read = 1;
	char* buf = res;
	while (nb_read_total < res_size && nb_read != 0) {
		nb_read = SDL_RWread(rw, buf, 1, (res_size - nb_read_total));
		nb_read_total += nb_read;
		buf += nb_read;
	}
	SDL_RWclose(rw);
	if (nb_read_total != res_size) {
		free(res);
		return NULL;
	}

	res[nb_read_total] = '\0';
	return res;
}
```

## Related Functions

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryIO](CategoryIO)


