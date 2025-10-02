from PIL import Image

class Utils:
    @staticmethod
    def read_image(filepath):
        try:
            img = Image.open(filepath).convert('L')
            pixels = list(img.getdata())
            width, height = img.size
            image = []
            for i in range(height):
                row = []
                for j in range(width):
                    row.append(float(pixels[i * width + j]))
                image.append(row)
            return image
        except ImportError:
            pass
        except Exception as e:
            print(f"Read error: {e}")
            return None
        
        try:
            with open(filepath, 'rb') as f:
                header = f.readline().decode().strip()
                if header != 'P5':
                    raise ValueError('Not a valid PGM file')
                
                dimensions = f.readline().decode().strip()
                while dimensions.startswith('#'):
                    dimensions = f.readline().decode().strip()
                width, height = map(int, dimensions.split())
                
                maxval = int(f.readline().decode().strip())
                if maxval > 255:
                    raise ValueError('Only 8-bit PGM files are supported')
                
                pixels = f.read()
                if len(pixels) != width * height:
                    raise ValueError('Pixel data does not match specified dimensions')
                
                image = []
                for i in range(height):
                    row = []
                    for j in range(width):
                        row.append(float(pixels[i * width + j]))
                    image.append(row)
                
                return image
        except Exception as e:
            print(f"Read error: {e}")
            return None


    @staticmethod
    def save_image(image, filepath):
        height = len(image)
        width = len(image[0])
        try:
            pixels = []
            for i in range(height):
                for j in range(width):
                    val = int(max(0, min(255, image[i][j])))
                    pixels.append(val)
            img = Image.new('L', (width, height))
            img.putdata(pixels)
            img.save(filepath)
            return
        except ImportError:
            pass
        except Exception as e:
            print(f"Save error: {e}")
        
        pgm_path = filepath.rsplit('.', 1)[0] + '.pgm'
        with open(pgm_path, 'wb') as f:
            f.write(b'P5\n')
            f.write(f'{width} {height}\n'.encode('ascii'))
            f.write(b'255\n')
            
            for i in range(height):
                for j in range(width):
                    val = int(max(0, min(255, image[i][j])))
                    f.write(bytes([val]))
        
        if pgm_path != filepath:
            print(f"Saved as {pgm_path} (Not available for {filepath})")
    
    @staticmethod
    def read_image_with_library(filepath):
        try:
            img = Image.open(filepath).convert('L')
            pixels = list(img.getdata())
            width, height = img.size
            image = []
            for i in range(height):
                row = []
                for j in range(width):
                    row.append(float(pixels[i * width + j]))
                image.append(row)
            return image
        except ImportError:
            print("Error reading image with PIL.")
            return None
    
    @staticmethod
    def save_image_with_library(image, filepath):
        try:
            height = len(image)
            width = len(image[0])
            pixels = []
            for i in range(height):
                for j in range(width):
                    val = int(max(0, min(255, image[i][j])))
                    pixels.append(val)
            img = Image.new('L', (width, height))
            img.putdata(pixels)
            img.save(filepath)
        except ImportError:
            print("Error saving image with PIL.")