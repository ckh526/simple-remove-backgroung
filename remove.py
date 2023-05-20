from rembg import remove
from PIL import Image
input_p = 'cute_cat.png'
output_p = 'out.png'
input = Image.open(input_p)
output = remove(input)
output.save(output_p)
