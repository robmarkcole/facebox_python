# facebox_python
A python script `teach.py` to teach [Machinebox/Facebox](https://machinebox.io/) from a directory containing folders with images, where the folder name is the name of the person to teach. The directory must contain folders with the layout:

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
Allowed extensions for training/teaching are: `.jpg`, `.png` and `.jpeg`

**Remember** with a free license of Machinebox/Facebox you are allowed to teach only 20 faces.
Run `teach.py` from the command line in the root directory containing all the folders. At the end of the teaching process the file `failed_log.txt` will be written. This file logs all failed teaching of faces, allowing you to check why an image has failed to be taught.
