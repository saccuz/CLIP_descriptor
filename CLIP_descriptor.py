from InquirerPy import prompt
from InquirerPy.separator import Separator
from PIL import Image

out_file = input("Destination file:")

out = open(out_file, 'a')
out.write('[')

to_label = '_to_label.txt'
folder = input("Source file:")

cat = {'message': 'Seleziona category:',
'type': 'list',
'choices': ['art_painting', 'cartoon', 'photo','sketch']
}

details = {'message': 'Details:',
'type': 'list',
'choices': ['high level details', 'mid level details', 'low level details']
}

edges = {'message': 'Edges:',
'type': 'checkbox',
'choices': ['definite strokes', 'precise strokes', 'neat strokes', 'definite brush strokes', 'precise brush strokes', 'neat brush strokes', Separator(), 'jagged'],
'height': 8
}

saturation = {'message': 'Color Saturation:',
'type': 'list',
'choices': ['high', 'mid', 'low']
}

shades = {'message': 'Color Shades:',
'type': 'input'
}

background = {'message': 'Background:',
'type': 'input'}

instance = {'message': 'Instance:',
'type': 'list',
'choices': ['single', 'multiple']}

text_ = {'message': 'Text:',
'type': 'checkbox',
'choices': ['with text', 'without text', Separator(), 'dense text', 'sparse text'],
'height': 5
}

texture = {'message': 'Texture',
'type': 'list',
'choices': ['with texture', 'without texture'],
'height': 4
}

tex_followup = {'message': 'Specifica texture:',
'type': 'input',
'when': lambda r: r[4] == 'with texture'}

perspective = {'message': 'Perspective:',
'type': 'list',
'choices': ['unrealistic', 'realistic']}

questions = [details,edges,saturation]
questions2 = [shades,background,instance,text_,texture,tex_followup,perspective]

result = prompt(cat)
category = result[0]
text_file = category + to_label

with open(folder + text_file) as f:
    for line in f:
        name = line.split(' ')[0]
        right = False
        with Image.open('PACS/kfold/'+name) as img:
            while not right:
                img.show()
                result = prompt(questions)
                res = prompt(questions2)
                if res[5] == None:
                    res[5] = ''
                desc = '{' + '\'image name\'' + ': ' + '\'' + name +'\'' + ', \'category\'' + ': ' + '\'' + category + '\'' + \
                '\'descriptions\'' + ': [' + '\'' + result[0] + '\', ' + '\'' + ", ".join(map(str,result[1])) + '\', ' + '\'' + result[2] + '\', ' \
                    + '\'' + res[0] + '\', ' + '\'' + res[1] + '\', ' + '\'' + res[2] + '\', ' + '\'' + ", ".join(map(str,res[3])) \
                        + '\', ' + '\'' + res[4] + ', ' +res[5] + '\', ' + '\'' + res[6] + '\''+ ']}, '
                value = input("Parametri giusti? (y/N)")
                if value == 'y' or value == 'Y':
                    right = True
                    out.write(desc)
out.write(']')
out.close()