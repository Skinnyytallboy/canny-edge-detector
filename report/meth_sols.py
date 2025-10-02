import math

class MathematicalProblems:    
    @staticmethod
    def problem1_gaussian_derivatives(sigma=1.0, size=50):
        step = 0.1
        coords = []
        x_val = -size / 2
        while x_val <= size / 2:
            coords.append(x_val)
            x_val += step
        G_1d = []
        dG_dx_1d = []
        d2G_dx2_1d = []
        
        for x in coords:
            g = math.exp(-x**2 / (2 * sigma**2))
            G_1d.append(g)
            dg = (-x / (sigma**2)) * g
            dG_dx_1d.append(dg)
            d2g = ((x**2 - sigma**2) / (sigma**4)) * g
            d2G_dx2_1d.append(d2g)
        X_2d = []
        Y_2d = []
        G_2d = []
        dG_dx_2d = []
        dG_dy_2d = []
        d2G_dx2_2d = []
        d2G_dy2_2d = []
        
        for x in coords:
            row_x = []
            row_y = []
            row_g = []
            row_dgx = []
            row_dgy = []
            row_d2gx = []
            row_d2gy = []
            
            for y in coords:
                row_x.append(x)
                row_y.append(y)
                
                g = math.exp(-(x**2 + y**2) / (2 * sigma**2))
                row_g.append(g)
                dgx = (-x / (sigma**2)) * g
                row_dgx.append(dgx)
                dgy = (-y / (sigma**2)) * g
                row_dgy.append(dgy)
                d2gx = ((x**2 - sigma**2) / (sigma**4)) * g
                row_d2gx.append(d2gx)
                d2gy = ((y**2 - sigma**2) / (sigma**4)) * g
                row_d2gy.append(d2gy)
            
            X_2d.append(row_x)
            Y_2d.append(row_y)
            G_2d.append(row_g)
            dG_dx_2d.append(row_dgx)
            dG_dy_2d.append(row_dgy)
            d2G_dx2_2d.append(row_d2gx)
            d2G_dy2_2d.append(row_d2gy)
        
        return {
            '1d': {
                'x': coords,
                'G': G_1d,
                'dG_dx': dG_dx_1d,
                'd2G_dx2': d2G_dx2_1d
            },
            '2d': {
                'X': X_2d,
                'Y': Y_2d,
                'G': G_2d,
                'dG_dx': dG_dx_2d,
                'dG_dy': dG_dy_2d,
                'd2G_dx2': d2G_dx2_2d,
                'd2G_dy2': d2G_dy2_2d
            }
        }
    


if __name__ == "__main__":
    math_problems = MathematicalProblems()
    
    print("Problem 1: Gaussian Derivatives")
    derivatives = math_problems.problem1_gaussian_derivatives(sigma=1.0)
    print("Calculated 1D and 2D Gaussian derivatives")
    print("Use matplotlib to plot these results\n")
