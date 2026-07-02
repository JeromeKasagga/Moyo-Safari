from PIL import Image
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IN = os.path.join(SCRIPT_DIR, '..', 'Frontend', 'assets', 'moyo_logo.jpeg')
OUT = os.path.join(SCRIPT_DIR, '..', 'Frontend', 'assets', 'moyo_logo.png')

def make_transparent(in_path=IN, out_path=OUT, tolerance=220):
    im = Image.open(in_path).convert("RGBA")
    datas = im.getdata()

    newData = []
    for item in datas:
        # item is (r,g,b,a)
        r, g, b, a = item
        # if pixel is near-white, make transparent
        if r >= tolerance and g >= tolerance and b >= tolerance:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((r, g, b, a))

    im.putdata(newData)
    im.save(out_path, "PNG")
    print(f"Saved transparent PNG to: {out_path}")

if __name__ == '__main__':
    try:
        in_path = sys.argv[1] if len(sys.argv) > 1 else IN
        out_path = sys.argv[2] if len(sys.argv) > 2 else OUT
        make_transparent(in_path, out_path)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
