# coding=utf-8
"""Calculate NDVI from a Landsat 8 scene."""

# For more information about landsat 8 bands, see:
# https://www.usgs.gov/media/images/landsat-8-band-designations
# https://landsat.gsfc.nasa.gov/landsat-8/landsat-8-bands/
# https://www.usgs.gov/faqs/how-does-data-sentinel-2a-s-multispectral-instrument-compare-landsat-data
RED_2013 = "data/120m/LC08_L1TP_042034_20130605_20170310_01_T1_B4_120x120.TIF"
NIR_2013 = "data/120m/LC08_L1TP_042034_20130605_20170310_01_T1_B5_120x120.TIF"
RED_2016 = "data/120m/LC08_L1TP_042034_20160629_20170222_01_T1_B4_120x120.TIF"
NIR_2016 = "data/120m/LC08_L1TP_042034_20160629_20170222_01_T1_B5_120x120.TIF"


def ndvi(red, nir):
    """Calculate NDVI for a Landsat 8 scene.

    For more information about NDVI, see:
    https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index

    Parameters:
        red (numpy.ndarray) - a numpy array of the red band for a Landsat 8
            scene.
        nir (numpy.ndarray) - a numpy array of the near-infrared band for a
            Landsat 8 scene.

    Returns:
        A ``numpy.ndarray`` with the calculated NDVI.
    """
    pass


if __name__ == '__main__':
    pass
