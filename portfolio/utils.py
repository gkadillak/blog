from unipath import Path
from datetime import datetime


def create_photo_directory(headline, *datetime_obj):
    """
    Given a datetime object, create a directory in
    portfolio/static/portfolio/media labeled YEAR_MONTH_DAY_HEADLINE

    input: python datetime object
    output: boolean indicating success or failure of directory creation
    """
    if not datetime_obj:
        datetime_obj = datetime.now()
    underscore_headline = headline.replace(' ', '_')
    post_dir = datetime_obj.strftime('%Y_%m_%d_{}'.format(underscore_headline))
    media_dir = Path('./portfolio/static/portfolio/media/{}'.format(post_dir))
    return media_dir.mkdir()
