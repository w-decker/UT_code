from nilearn import datasets, plotting
import numpy as np


def plot_rois(roi, cmap):
    """Plot cortical ROIs
    
    Parameters
    ----------
    roi: int

    cmap: str

    Return
    ------
    p: matplotlib object
    """

    # get atlas
    atlas = datasets.fetch_atlas_surf_destrieux()

    # hemisphere
    hemi = atlas['map_left']

    # mask
    mask = np.zeros_like(hemi, dtype=float)
    roi_indices = np.where(hemi == roi)
    mask[roi_indices] = np.random.uniform(0.1, 10, size=len(roi_indices[0]))

    # fsaverage
    fsaverage = datasets.fetch_surf_fsaverage()
    fscat = 'pial_left'

    p = plotting.plot_surf_roi(fsaverage[fscat], roi_map=mask,
                                hemi='left', view='lateral',
                                bg_map=fsaverage['sulc_left'], bg_on_data=True,
                                darkness=.5, cmap=cmap)