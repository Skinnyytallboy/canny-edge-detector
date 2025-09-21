# Roll No.:         BSCS23134
# Name:             Jalal Ahmed
# Assignment No.:   02


import argparse

def main(args):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Canny's Edge Detector")
    parser.add_argument("--input_folder", type=str, required=True, help="path_to_input_folder")
    parser.add_argument("--output_folder", type=str, required=True, help="path_to_output_folder")
    parser.add_argument("--input_ext", type=str, default="png", help="path_to_input_folder")
    parser.add_argument("--output_ext", type=str, default="png", help="path_to_output_folder")

    args = parser.parse_args()
    main(args)