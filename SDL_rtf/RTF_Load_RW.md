====== (This function is part of SDL_rtf, a separate library from SDL.) ======
= RTF_Load_RW =

Set the text of an RTF context, with data loaded from an SDL_RWops.

== Syntax ==

<syntaxhighlight lang='c'>
int RTF_Load_RW(RTF_Context *ctx, SDL_RWops *src, int freesrc);
</syntaxhighlight>

== Function Parameters ==

{|
|'''ctx'''
|the RTF context to update.
|-
|'''src'''
|the SDL_RWops to load RTF data from.
|-
|'''freesrc'''
|non-zero to close/free <code>src</code>, zero to leave open.
|}

== Return Value ==

Returns 0 on success, -1 on failure.

== Remarks ==

This can be called multiple times to change the text displayed.

If <code>freesrc</code> is non-zero, this function will close/free
<code>src</code>, whether this function succeeded or not.

On failure, call [[RTF_GetError]]() to get a human-readable text message
corresponding to the error.

== Version ==

This function is available since SDL_rtf 2.0.0.

----
[[CategoryAPI]]


