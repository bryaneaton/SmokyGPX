from lxml import html
import requests, os


def getGPXNames(url):
    page = requests.get(url)
    webpage = html.fromstring(page.content)

    links = webpage.xpath('//a/@href')
    gpx = [x for x in links if 'gpx' in x]
    return gpx



if __name__ == '__main__':

    site = 'http://tnlandforms.us/data/g/'
    save_folder = '/home/bryan/Documents/GSMNP_Files'

    gpx = getGPXNames(site)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    #Loop through page and save gpx files
    for g in gpx:
        url = site + g
        r = requests.get(url)
        print("Saving file {0}..".format(g))
        with open(save_folder + os.sep + g, 'wb') as f:
            f.write(r.content)






