# pianoTilesBot

this bot, once activated, will automatically play piano tiles online.
it will detect and perss the tiles on the screen.

pianotiles bot 1.0: works with a single thread, iterating over the four rows on your screen.
pianotiles bot 2.0: works with multiple threards, each one checks it's own row. => the result is a lot more speed and accuracy.
pianotiles bot 3.0: this model works with 4 threads and uses keyboard buttons insted of mouse clicks. this multiplies the maximum score this bot can achive by 15.

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
