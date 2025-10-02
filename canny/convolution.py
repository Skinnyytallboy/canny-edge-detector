


class Convolution:
    @staticmethod
    def convolve(image, kernel):
        img_height = len(image)
        img_width = len(image[0])
        kernel_height = len(kernel)
        kernel_width = len(kernel[0])
        pad_h = kernel_height // 2
        pad_w = kernel_width // 2
        output = []
        for i in range(img_height):
            row = []
            for j in range(img_width):
                row.append(0.0)
            output.append(row)
        
        for i in range(img_height):
            for j in range(img_width):
                sum_val = 0.0
                for ki in range(kernel_height):
                    for kj in range(kernel_width):
                        ii = i + ki - pad_h
                        jj = j + kj - pad_w
                        if 0 <= ii < img_height and 0 <= jj < img_width:
                            sum_val += image[ii][jj] * kernel[ki][kj]
                output[i][j] = sum_val
        
        return output