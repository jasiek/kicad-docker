## Usage

```
$ docker pull jasiek/kicad
$ cd where/is/my/project
$ docker run --rm -v $(pwd):/source jasiek/kicad projectname.kicad_pcb
```

## TODO

* ~~Plot fabrication artifacts suitable for toner/transparency DIY work.~~
* ~~Plot drill files.~~
* Plot PNG previews of boards.

## Resources

* http://gerbv.geda-project.org/doxygen/example3_8c-example.html
* https://github.com/bleepbloop/absolum/blob/master/gerbv/viewer.py
