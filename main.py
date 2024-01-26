from utils import *
import matplotlib.pyplot as plt
from config import IMAGES_DIR

# some brain plots

p1 = plot_rois(roi=34, cmap='YlOrBr')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_1.png')
p2 = plot_rois(roi=34, cmap='afmhot')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_2.png')
p3 = plot_rois(roi=25, cmap='winter')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_3.png')
p4 = plot_rois(roi=25, cmap='afmhot')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_4.png')

p5 = plot_glass(cmap='afmhot', threshold=2)
plt.savefig(f'{IMAGES_DIR}/glass_1.png')
p6 = plot_glass(cmap='afmhot', threshold=1.5)
plt.savefig(f'{IMAGES_DIR}/glass_2.png')