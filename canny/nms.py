
class NMS:
    @staticmethod
    def quantize_direction(angle):
        if (0 <= angle < 22.5) or (157.5 <= angle < 202.5) or (337.5 <= angle <= 360):
            return 0
        elif (22.5 <= angle < 67.5) or (202.5 <= angle < 247.5):
            return 1
        elif (67.5 <= angle < 112.5) or (247.5 <= angle < 292.5):
            return 2
        else:
            return 3
    
    def apply(self, magnitude, direction):
        height = len(magnitude)
        width = len(magnitude[0])
        quantized = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(self.quantize_direction(direction[i][j]))
            quantized.append(row)
        
        suppressed = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0.0)
            suppressed.append(row)
        
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                q = quantized[i][j]
                current = magnitude[i][j]
                if q == 0:
                    neighbor1 = magnitude[i][j - 1]
                    neighbor2 = magnitude[i][j + 1]
                elif q == 1:
                    neighbor1 = magnitude[i - 1][j - 1]
                    neighbor2 = magnitude[i + 1][j + 1]
                elif q == 2:
                    neighbor1 = magnitude[i - 1][j]
                    neighbor2 = magnitude[i + 1][j]
                else:
                    neighbor1 = magnitude[i - 1][j + 1]
                    neighbor2 = magnitude[i + 1][j - 1]
                if current >= neighbor1 and current >= neighbor2:
                    suppressed[i][j] = current
                else:
                    suppressed[i][j] = 0.0
        
        quantized_vis = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(quantized[i][j] * 85)
            quantized_vis.append(row)
        
        return suppressed, quantized_vis