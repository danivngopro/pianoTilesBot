# pianoTilesBot

this bot, once activated, will automatically play piano tiles online.
it will detect and perss the tiles on the screen.


the way it works:
1) i have detected a small chunk on the screen there the tiles are dropping to.
2) i used mss to take a screenshot of this small chunk.
3) the chunk is divided to 4 bits, each bit represents a position where a tile might be.
4) i use the screenshot to detect a blue/black color.
5) if a blue/black color is found, click it!


alert:
  the pixels on your screen may change due to width diffrences. ajust the width to your satisfaction
  
  you can use get_mouse_pos and get_pixel_color to detect the colors and positions in your screen.


link to the online piano tiles 2 i used: https://poki.co.il/g/piano-tiles-2
