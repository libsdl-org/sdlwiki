###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWops

This is the read/write operation structure -- very basic.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
typedef struct SDL_RWops
{
    /**
     *  Return the size of the file in this rwops, or -1 if unknown
     */
    Sint64 (SDLCALL * size) (struct SDL_RWops * context);

    /**
     *  Seek to \c offset relative to \c whence, one of stdio's whence values:
     *  RW_SEEK_SET, RW_SEEK_CUR, RW_SEEK_END
     *
     *  \return the final offset in the data stream, or -1 on error.
     */
    Sint64 (SDLCALL * seek) (struct SDL_RWops * context, Sint64 offset,
                             int whence);

    /**
     *  Read up to \c maxnum objects each of size \c size from the data
     *  stream to the area pointed at by \c ptr.
     *
     *  \return the number of objects read, or 0 at error or end of file.
     */
    size_t (SDLCALL * read) (struct SDL_RWops * context, void *ptr,
                             size_t size, size_t maxnum);

    /**
     *  Write exactly \c num objects each of size \c size from the area
     *  pointed at by \c ptr to data stream.
     *
     *  \return the number of objects written, or 0 at error or end of file.
     */
    size_t (SDLCALL * write) (struct SDL_RWops * context, const void *ptr,
                              size_t size, size_t num);

    /**
     *  Close and free an allocated SDL_RWops structure.
     *
     *  \return 0 if successful or -1 on write error when flushing data.
     */
    int (SDLCALL * close) (struct SDL_RWops * context);

    Uint32 type;
    union
    {
#if defined(__ANDROID__)
        struct
        {
            void *asset;
        } androidio;
#elif defined(__WIN32__) || defined(__GDK__)
        struct
        {
            SDL_bool append;
            void *h;
            struct
            {
                void *data;
                size_t size;
                size_t left;
            } buffer;
        } windowsio;
#endif

#ifdef HAVE_STDIO_H
        struct
        {
            SDL_bool autoclose;
            FILE *fp;
        } stdio;
#endif
        struct
        {
            Uint8 *base;
            Uint8 *here;
            Uint8 *stop;
        } mem;
        struct
        {
            void *data1;
            void *data2;
        } unknown;
    } hidden;

} SDL_RWops;
```

## Code Examples

```c++
SDL_RWops *io = SDL_RWFromFile("username.txt", "rb");
if (io != NULL) {
    char name[256];
    if (io->read(io, name, sizeof (name), 1) > 0) {
        printf("Hello, %s!\n", name);
    }
    io->close(io);
}
```

The following is functionally identical to the above example, but uses the recommended macro interface.

```c++
SDL_RWops *io = SDL_RWFromFile("username.txt", "rb");
if (io != NULL) {
    char name[256];
    if (SDL_RWread(io, name, sizeof (name), 1) > 0) {
        printf("Hello, %s!\n", name);
    }
    SDL_RWclose(io);
}
```

## Data Fields

{|
|Sint64 (*)(SDL_RWops *)
|'''size'''
|callback that reports stream size; see [[#Size Function|Remarks]]
|-
|Sint64 (*)(SDL_RWops *, Sint64, int)
|'''seek'''
|callback that seeks in stream; see [[#Seek Function|Remarks]]
|-
|size_t (*)(SDL_RWops *, void *, size_t, size_t)
|'''read'''
|callback that reads from the stream; see [[#Read Function|Remarks]]
|-
|size_t (*)(SDL_RWops *, const void *, size_t, size_t)
|'''write'''
|callback that writes to the stream; see [[#Write Function|Remarks]]
|-
|int (*)(SDL_RWops *)
|'''close'''
|callback that closes the stream; see [[#Close Function|Remarks]]
|-
|Uint32
|'''type'''
|type of stream; see [[#Stream Type|Remarks]]
|-
|union
|'''hidden'''
|type-specific data; see [[#Hidden Union|Remarks]]
|}

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryIO](CategoryIO)


