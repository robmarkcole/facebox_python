A python script `teach_facebox.py` to teach [Machinebox/Facebox](https://machineboxio.com/docs/facebox) from a directory containing folders with images of faces, where the folder name is the name of the person/face to teach. The directory must contain folders of images with the structure:

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
Allowed extensions for images are: `.jpg`, `.jpeg` and `.png`.

**Usage** Run `teach_facebox.py` from the command line in the directory containing all the folders of images. The script assumes your Facebox is running on `localhost`, if this isn't the case you will need to edit `teach_api_url` and `health_api_url` in `teach_facebox.py`.

**Limits** With a free license of Facebox you are limited to teaching 20 faces.

**Output** At the end of the teaching process the file `failed_log.txt` will be written. This file logs all failed teaching of faces, allowing you to check why an image has failed to be taught.
