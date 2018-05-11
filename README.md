A python script `teach.py` to teach [Machinebox/Facebox](https://machineboxio.com/docs/facebox) from a directory containing folders with images, where the folder name is the name of the person to teach. The directory must contain folders of images with the structure:

```bash
person_1/
    img1.jpg
    img2.jpg
    ........
person_2/
    image1.png
    image2.png
    ..........
person_3/
    image1.jpeg
    image2.jpeg
    ..........    
```
Allowed extensions for images are: `.jpg`, `.png` and `.jpeg`

**Usage** Run `teach.py` from the command line in the root directory containing all the folders.

**Limits** With a free license of Machinebox/Facebox you are limited to teaching 20 faces.

**Output** At the end of the teaching process the file `failed_log.txt` will be written. This file logs all failed teaching of faces, allowing you to check why an image has failed to be taught.
