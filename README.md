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
Allowed file extensions for images are: `.jpg`, `.jpeg` and `.png`.

**Usage** Run `teach_facebox.py` from the command line in the directory containing all the folders of images. The script assumes your Facebox is running on `localhost:8080` and that it does not need authentication, if this isn't the case you will need to edit the `IP`, `PORT`, `USERNAME` and `PASSWORD` variables in `teach_facebox.py`.

**Limits** With a free license of Facebox you are limited to teaching 100 faces.

## State file

Once you have trained facebox you can download the state file using:
```curl
curl -o state.facebox http://localhost:8080/facebox/state
```

If you restart facebox and lose the state, you can upload your saved state file using:
```curl
curl -X POST -F 'file=@state.facebox' http://localhost:8080/facebox/state
```
