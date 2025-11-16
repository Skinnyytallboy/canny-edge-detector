# Canny Edge Detection

## Overview

This project implements the Canny Edge Detection algorithm from scratch using pure Python. The implementation includes all major steps of the Canny algorithm:

1. **Gaussian Filtering** - Noise reduction using Gaussian derivatives
2. **Gradient Computation** - Calculate gradient magnitude and direction
3. **Non-Maximum Suppression** - Thin edges to single pixel width
4. **Hysteresis Thresholding** - Connect edge pixels using high/low thresholds

## Features

- **Flexible Input**: Accepts both single image files and entire directories
- **Multiple Sigma Values**: Tests edge detection with different Gaussian sigma values (0.5, 1.0, 2.0)
- **Threshold Comparison**: Compares different hysteresis threshold combinations
- **Comprehensive Visualization**: Creates single images showing all processing steps instead of cluttering with many separate files
- **Multiple Image Formats**: Supports JPG, PNG, TIF, BMP formats

## Usage

### Single Image Processing
```bash
python main.py --input data/circle.jpg --output_folder results/
```

### Directory Processing
```bash
python main.py --input data/ --output_folder results/
```

### Custom Extensions
```bash
python main.py --input data/ --output_folder results/ --input_ext tif --output_ext jpg
```

## Output Files

For each input image, the following visualization files are generated:

1. **`{image}_sigma_{value}_complete.png`** - Shows all processing steps:
   - Original image
   - Gradient X
   - Gradient Y  
   - Gradient magnitude
   - Quantized directions
   - Non-maximum suppression result
   - Final edge detection

2. **`{image}_sigma_1.0_Th{high}_Tl{low}.png`** - Threshold comparison:
   - Original image
   - Gradient magnitude
   - NMS result
   - Edges with specific thresholds

## Implementation Structure

- `main.py` - Entry point and argument handling
- `canny/canny.py` - Main Canny edge detector class
- `canny/filters.py` - Gaussian filter and derivative generation
- `canny/convolution.py` - Convolution operations
- `canny/gradient.py` - Gradient magnitude and direction computation
- `canny/nms.py` - Non-maximum suppression
- `canny/hysteresis.py` - Hysteresis thresholding
- `canny/utils.py` - Image I/O and visualization utilities
