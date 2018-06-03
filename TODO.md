### Including Package Data

Currently, the website package data (CSS/JS files) is place under `wgal/website/`. I don't think this is a particularly elegant approach.  
However, package data, as the name suggests, must be placed in a package. Consequently I must place it inside `wgal/` as this is the only package supplied in this project. 
In the later stages of this project, we will need `string.Template` files also to be stored as package data. Until then, I may create a new data package to be included.  
On the other hand, perhaps placing the data in `wgal/` is the only sensible option.
