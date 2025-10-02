import math

class Filters:
    def __init__(self, sigma=1.0, T=0.3):
        self.sigma = sigma
        self.T = T
        self.filter_size = self.calculate_filter_size(sigma, T)
    
    @staticmethod
    def calculate_filter_size(sigma, T):
        sHalf = round(math.sqrt(-math.log(T) * 2 * sigma**2))
        N = 2 * sHalf + 1
        return N
    
    def create_meshgrid(self):
        sHalf = (self.filter_size - 1) // 2
        X = []
        Y = []
        for i in range(-sHalf, sHalf + 1):
            row_x = []
            row_y = []
            for j in range(-sHalf, sHalf + 1):
                row_x.append(j)
                row_y.append(i)
            X.append(row_x)
            Y.append(row_y)
        
        return X, Y
    
    def gaussian(self, x, y):
        return math.exp(-(x**2 + y**2) / (2 * self.sigma**2))
    
    def gaussian_derivative_x(self, x, y):
        return (-x / (self.sigma**2)) * self.gaussian(x, y)
    
    def gaussian_derivative_y(self, x, y):
        return (-y / (self.sigma**2)) * self.gaussian(x, y)
    
    def get_derivative_masks(self):
        X, Y = self.create_meshgrid()
        Gx = []
        Gy = []
        for i in range(len(X)):
            row_gx = []
            row_gy = []
            for j in range(len(X[0])):
                row_gx.append(self.gaussian_derivative_x(X[i][j], Y[i][j]))
                row_gy.append(self.gaussian_derivative_y(X[i][j], Y[i][j]))
            Gx.append(row_gx)
            Gy.append(row_gy)
        
        scale_factor = 255.0
        Gx_scaled = []
        Gy_scaled = []
        
        for i in range(len(Gx)):
            row_gx = []
            row_gy = []
            for j in range(len(Gx[0])):
                row_gx.append(round(Gx[i][j] * scale_factor))
                row_gy.append(round(Gy[i][j] * scale_factor))
            Gx_scaled.append(row_gx)
            Gy_scaled.append(row_gy)
        
        return Gx_scaled, Gy_scaled, scale_factor