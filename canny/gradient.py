import math

class Gradients:
    def __init__(self, scale_factor=1.0):
        self.scale_factor = scale_factor
    
    def compute_magnitude(self, fx, fy):
        height = len(fx)
        width = len(fx[0])
        
        magnitude = []
        max_val = 0.0
        min_val = float('inf')
        
        for i in range(height):
            row = []
            for j in range(width):
                mag = math.sqrt(fx[i][j]**2 + fy[i][j]**2)
                mag = mag / self.scale_factor
                row.append(mag)
                
                if mag > max_val:
                    max_val = mag
                if mag < min_val:
                    min_val = mag
            magnitude.append(row)
        
        magnitude_scaled = []
        for i in range(height):
            row = []
            for j in range(width):
                if max_val > min_val:
                    val = (magnitude[i][j] - min_val) * 255.0 / (max_val - min_val)
                else:
                    val = 0
                row.append(val)
            magnitude_scaled.append(row)
        
        return magnitude_scaled
    
    def compute_direction(self, fx, fy):
        height = len(fx)
        width = len(fx[0])
        direction = []
        for i in range(height):
            row = []
            for j in range(width):
                angle_rad = math.atan2(fy[i][j], fx[i][j])
                angle_deg = math.degrees(angle_rad)
                angle_deg = angle_deg + 180.0
                row.append(angle_deg)
            direction.append(row)
        
        return direction