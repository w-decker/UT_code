from nilearn import datasets, plotting


def plot_rois(roi):
    """Plot cortical ROIs
    
    Parameters
    ----------
    roi: int

    name: str

    filename: str

    Return
    ------
    p: matplotlib object
    """

    # get atlas
    atlas = datasets.fetch_atlas_surf_destrieux()

    # hemisphere
    hemi = atlas['map_left']

    # mask
    mask = (hemi == roi)

    # fsaverage
    fsaverage = datasets.fetch_surf_fsaverage()
    fscat = 'pial_left'

    p = plotting.plot_surf_roi(fsaverage[fscat], roi_map=mask,
                                hemi='left', view='lateral',
                                bg_map=fsaverage['sulc_left'], bg_on_data=True,
                                darkness=.5, cmap='YlOrBr')