from utils import *
import matplotlib.pyplot as plt
from config import IMAGES_DIR

# some brain plots

p = plot_rois(roi=34, cmap='YlOrBr')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_1.png')
pp = plot_rois(roi=34, cmap='afmhot')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_2.png')
ppp = plot_rois(roi=25, cmap='winter')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_3.png')
pppp = plot_rois(roi=25, cmap='afmhot')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_4.png')
r = list(np.arange(1, 53))
ppppp = plot_rois(roi=r, cmap='afmhot')
plt.savefig(f'{IMAGES_DIR}/ut_univar_roi_6.png')

pppppp = plot_glass(cmap='afmhot', threshold=2)
plt.savefig(f'{IMAGES_DIR}/glass_1.png')
ppppppp = plot_glass(cmap='afmhot', threshold=1.5)
plt.savefig(f'{IMAGES_DIR}/glass_2.png')