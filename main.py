# Roll No.:         BSCS23134
# Name:             Jalal Ahmed
# Assignment No.:   02


import os
import argparse
from canny.utils import Utils
from canny.canny import CannyEdgeDetector

def main():
    parser = argparse.ArgumentParser(description='Canny Edge Detection')
    parser.add_argument('--input', type=str, required=True, help='Path to input image file or folder')
    parser.add_argument('--output_folder', type=str, required=True, help='Path to output folder')
    parser.add_argument('--input_ext', type=str, default='jpg', help='Input image extension (for folder processing)')
    parser.add_argument('--output_ext', type=str, default='png', help='Output image extension')
    
    args = parser.parse_args()
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    image_files = []
    input_paths = []
    if os.path.isfile(args.input):
        if args.input.lower().endswith(('.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp')):
            image_files = [os.path.basename(args.input)]
            input_paths = [args.input]
        else:
            print(f"Error: {args.input} is not a valid image file")
            return
    elif os.path.isdir(args.input):
        valid_extensions = ['.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp']
        image_files = [f for f in os.listdir(args.input) 
                      if any(f.lower().endswith(ext) for ext in valid_extensions)]
        input_paths = [os.path.join(args.input, f) for f in image_files]
    else:
        print(f"Error: {args.input} is not a valid file or directory")
        return
    
    if not image_files:
        print("No valid image files found")
        return
    for i, (image_file, input_path) in enumerate(zip(image_files, input_paths)):
        print(f"Processing {image_file}...")
        
        try:
            image = Utils.read_image(input_path)
            if image is None:
                print(f"  Error: Could not read {image_file}")
                continue
            base_name = os.path.splitext(image_file)[0]
            sigma_values = [0.5, 1.0, 2.0]
            T = 0.3
            for sigma in sigma_values:
                print(f"  Processing with sigma={sigma}")
                detector = CannyEdgeDetector(sigma=sigma, T=T)
                results = detector.process(image)
                frames = [
                    image,  
                    results['fx'],
                    results['fy'],
                    results['magnitude'],
                    results['quantized'],
                    results['nms'],
                    results['edges']
                ]
                frame_titles = [
                    "Original",
                    "Gradient X",
                    "Gradient Y", 
                    "Magnitude",
                    "Quantized Directions",
                    "Non-Max Suppression",
                    "Final Edges"
                ]
                
                save_name = os.path.join(args.output_folder, f"{base_name}_sigma_{sigma}_complete.{args.output_ext}")
                Utils.plot_frames(frames, frame_titles, save_name)
            print(f"  Processing sigma=1.0 with different thresholds")
            detector = CannyEdgeDetector(sigma=1.0, T=T)
            results = detector.process(image)
            threshold_combos = [(100, 50), (150, 75)]
            for Th, Tl in threshold_combos:
                edges = detector.hysteresis_thresholding(results['nms'], Th=Th, Tl=Tl)
                comparison_frames = [
                    image,
                    results['magnitude'],
                    results['nms'],
                    edges
                ]
                
                comparison_titles = [
                    "Original",
                    "Magnitude",
                    "NMS Result",
                    f"Edges (Th={Th}, Tl={Tl})"
                ]
                
                save_name = os.path.join(args.output_folder, f"{base_name}_sigma_1.0_Th{Th}_Tl{Tl}.{args.output_ext}")
                Utils.plot_frames(comparison_frames, comparison_titles, save_name)
                
        except Exception as e:
            print(f"  Error processing {image_file}: {e}")
            continue
    
    print("Processing complete!")

if __name__ == "__main__":
    main()