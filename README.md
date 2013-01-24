Sheboygan
=========

A script I wrote to mass download images from Reddit. This works really well with downloading images that are linked to Imgur but will fail if the image is linked to the page of another site instead of a direct link.

### Basic Usage

The program asks you for a subreddit which you then supply `wallpapers` after that it will ask for how many pages and will go and grab all the links and start to asynchronously grab all images. It saves all of the images under `./downloads/{subreddit}`. Under the subreddit folder it creates `gif` and `img` directories and saves the images accordingly.
