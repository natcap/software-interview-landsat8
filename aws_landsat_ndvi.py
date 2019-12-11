# coding=utf-8
"""Calculate NDVI from a full Landsat 8 scene."""

# Landsat scene index at https://landsatonaws.com/L8/042/034/
AWS_RED_2013 = "LC08_L1TP_042034_20130605_20170310_01_T1_B4.TIF"
AWS_NIR_2013 = "LC08_L1TP_042034_20130605_20170310_01_T1_B5.TIF"
AWS_RED_2016 = "LC08_L1TP_042034_20160629_20170222_01_T1_B4.TIF"
AWS_NIR_2016 = "LC08_L1TP_042034_20160629_20170222_01_T1_B5.TIF"

def get_aws_url(raster_id):
    """Given a landsat filename, download it from AWS.

    Parameters:
        raster_id (string): The local filename of a landsat 8 band to download
            from AWS.

    Returns:
        The fully-qualified HTTPS download path to the requested landsat
        raster.

    """
    landsat, product, pathrow = raster_id.split('_')[:3]

    landsat = '%s%s' % (landsat[0], landsat[3])
    path = pathrow[:3]
    row = pathrow[3:]
    scene = '_'.join(raster_id.split('_')[:-1])
    raster = raster_id

    return (
        f'https://landsat-pds.s3.amazonaws.com/c1/'
        f'{landsat}/{path}/{row}/{scene}/{raster}')


if __name__ == '__main__':
    pass
