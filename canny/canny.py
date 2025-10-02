from .filters import Filters
from .convolution import Convolution
from .gradient import Gradients
from .nms import NMS
from .hysteresis import Hysteresis

class CannyEdgeDetector:
    def __init__(self, sigma=1.0, T=0.3, Th=100, Tl=50):
        self.sigma = sigma
        self.T = T
        self.Th = Th
        self.Tl = Tl
        self.gaussian_filter = Filters(sigma, T)
        self.Gx, self.Gy, self.scale_factor = self.gaussian_filter.get_derivative_masks()
    
    def process(self, image):
        conv = Convolution()
        fx = conv.convolve(image, self.Gx)
        fy = conv.convolve(image, self.Gy)
        grad_processor = Gradients(self.scale_factor)
        magnitude = grad_processor.compute_magnitude(fx, fy)
        direction = grad_processor.compute_direction(fx, fy)
        nms = NMS()
        nms_result, quantized = nms.apply(magnitude, direction)
        hysteresis = Hysteresis()
        edges = hysteresis.apply(nms_result, self.Th, self.Tl)
        return {
            'fx': fx,
            'fy': fy,
            'magnitude': magnitude,
            'direction': direction,
            'quantized': quantized,
            'nms': nms_result,
            'edges': edges
        }
    
    def hysteresis_thresholding(self, nms_image, Th, Tl):
        hysteresis = Hysteresis()
        return hysteresis.apply(nms_image, Th, Tl)