from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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
    
    @staticmethod
    def plot_frames(frames: list, titles: list, save_name: str) -> None:
        try:
            num_frames = len(frames)
            if num_frames == 0:
                return
            if num_frames <= 4:
                rows, cols = 2, 2
            elif num_frames <= 6:
                rows, cols = 2, 3
            elif num_frames <= 8:
                rows, cols = 2, 4
            else:
                rows = int(np.ceil(np.sqrt(num_frames)))
                cols = int(np.ceil(num_frames / rows))
            plt.figure(figsize=(4 * cols, 3 * rows))
            for i in range(num_frames):
                plt.subplot(rows, cols, i + 1)
                frame_array = np.array(frames[i])
                plt.imshow(frame_array, cmap='gray', vmin=0, vmax=255)
                if i < len(titles):
                    plt.title(titles[i], fontsize=10)
                else:
                    plt.title(f"Frame {i}", fontsize=10)
                
                plt.axis('off')
            plt.tight_layout()
            plt.savefig(save_name, bbox_inches='tight', dpi=150)
            plt.close()
            
        except Exception as e:
            print(f"Error creating visualization: {e}")
            for i, frame in enumerate(frames):
                try:
                    title = titles[i] if i < len(titles) else f"frame_{i}"
                    fallback_name = save_name.replace('.', f'_{title}.') 
                    Utils.save_image(frame, fallback_name)
                except:
                    pass