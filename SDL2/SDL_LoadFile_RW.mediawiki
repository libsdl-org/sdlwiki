====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_LoadFile_RW =

Load all the data from an SDL data stream.

== Syntax ==

<syntaxhighlight lang='c'>
void* SDL_LoadFile_RW(SDL_RWops *src,
                      size_t *datasize,
                      int freesrc);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the [[SDL_RWops]] to read all available data from
|-
|'''datasize'''
|if not NULL, will store the number of bytes read
|-
|'''freesrc'''
|if non-zero, calls [[SDL_RWclose]]() on <code>src</code> before returning
|}

== Return Value ==

Returns the data, or NULL if there was an error.

== Remarks ==

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
<code>datasize</code>.

The data should be freed with [[SDL_free]]().

== Version ==

This function is available since SDL 2.0.6.

----
[[CategoryAPI]]


