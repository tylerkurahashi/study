import os
import glob
import argparse
import random
import cv2
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET
#-----------------------------------
# Purpose
# - Augment dataset by cropping images with random ratio 
# - Also generate xml files according to the original image
# Requirement 
# - Image
# - xml file 
#-----------------------------------

# img is a numpy array
class Split:
    def __init__(self, img, split_px) -> None:
        self.img = img
        self.height, self.width, self.dimension = self.img.shape
        self.splitted_img = None
        self.split_px = split_px
        self.column = self.width // self.split_px + 1
        self.row =  self.height // self.split_px + 1
        self.column_stride = self.width / (self.column - 1) - (split_px / 2)
        self.row_stride = self.height / (self.row - 1) - (split_px / 2)
        if split_px <= self.width and split_px <= self.height:    
            self.next_range = [split_px, split_px, self.dimension]     
    
    def next_range(self):
        return self.next_range

    def cut_image(self):
        return 

    def move_range(self):
        return

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()    
    parser.add_argument('--dataset')    
    args = parser.parse_args()
    uc = args.dataset    
    xml_path = '/home/tyler/Desktop/datasets/' + uc + '/'    
    img_path = '/home/tyler/Desktop/datasets/' + uc + '/'
    for f in glob.glob(xml_path + ''):
    img = np.array(Image.open(f))