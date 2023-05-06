A PARTIR DO REPOSITÓRIO DO BLACKAVEC, FORAM ADICIONADAS ALGUMAS FUNCIONALIDADES AO ALGORITMO:
I) Tira uma quantidade arbitrária de prints 
II) Guarda em uma pasta criada com o nome dado
III)...


# mp4-frame-extractor
a simple application written in python to export a frame of video to jpeg

## install
First of all, you need to set up `virtualenv`
```
# create new env
virtualenv env

# activate the environment
source ./env/bin/activate

# install dependencies
pip install -r requirement.txt
```

## running
```
python main.py -h

python main.py --video <path-to-video> --frame <frame-number> --out <output-dir>
```

example:
```
# this will take a shot from frame 4000 and export to the same directory as source code
python main.py --frame 4000 --video sample.mp4 --out ./
```
