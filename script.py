import json
import io
import pip
from pip._internal import main
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'dependecis': ["beautifulsoup4==4.4.1",
"boto==2.48.0",
"bz2file==0.98",
"certifi==2017.7.27.1",
"chardet==3.0.4",
"gensim==2.3.0",
"html5lib==0.999",
"idna==2.5",
"nltk==3.2.4",
"numpy==1.13.1",
"pexpect==4.0.1",
"pip==9.0.1",
"ptyprocess==0.5",
"pyxdg==0.25",
"reportlab==3.3.0",
"requests==2.18.3",
"scipy==0.19.1",
"setuptools==20.7.0",
"six==1.10.0",
"smart-open==1.5.3",
"textblob==0.12.0",
"twitter==1.17.1",
"urllib3==1.22"
]
        }

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

dependencies=data_loaded['dependecis']
print(len(dependencies))


def install(package):
    if hasattr(pip, 'main'):
        return pip.main(['install', package])
    else:
        return pip._internal.main(['install', package])
l=[]
flag=1
for i in dependencies:
    if not install(i):
        flag=0
        l.append(i)
if flag:
    print("succesfully installed")
print("------------------------------------------")
print("not installed dependecies ")
n1=len(l)
print(n1)
for i in l:
    print(i)
