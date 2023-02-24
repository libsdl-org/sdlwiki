====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_GetMusicCopyrightTag =

Get the copyright text for a music object.

== Syntax ==

<syntaxhighlight lang='c'>
const char* Mix_GetMusicCopyrightTag(const Mix_Music *music);
</syntaxhighlight>

== Function Parameters ==

{|
|'''music'''
|the music object to query, or NULL for the currently-playing music.
|}

== Return Value ==

Returns the music's copyright text if available, or "".

== Remarks ==

This returns format-specific metadata. Not all file formats supply this!

If <code>music</code> is NULL, this will query the currently-playing music.

This function never returns NULL! If no data is available, it will return
an empty string ("").

== Version ==

This function is available since SDL_mixer 2.6.0.

== Related Functions ==

:[[Mix_GetMusicTitleTag]]
:[[Mix_GetMusicArtistTag]]
:[[Mix_GetMusicAlbumTag]]

----
[[CategoryAPI]]


