from bs4 import BeautifulSoup
import requests

config = {
    'webpages' = [
        'https://mp.weixin.qq.com/s?__biz=MzA4MDY4OTMyMg==&mid=2652864427&idx=1&sn=10ac07e99e63cb07d2d2efe14d4790c3&chksm=844bbe6eb33c37782dd978b658d629d8e07a0482388dc40ca4352cde52ec7fc0139b669e72ba&mpshare=1&scene=1&srcid=0823YIa387D6AdSoBcyUfZGB&key=ec44f6d9f66b7680ccc85c3153e8fd4ff681abdf83753b8c86c5ceb6a0e6901e7266037583f352ab9af386299ae54f2922700ff2412efd09a2d27ed73ba9ef71a4a729d483f543b2e2c69e835a0a0ec2&ascene=0&uin=MTA5NTQxNTc1&devicetype=iMac+MacBookPro11%2C4+OSX+OSX+10.11.6+build(15G1611)&version=12020810&nettype=WIFI&fontScale=100&pass_ticket=uGchUv3CviAcxUhqpBB0q1c6U%2F2Zl06u%2BEzBOgEjolE%3D',
        'https://mp.weixin.qq.com/s?__biz=MzA4MDY4OTMyMg==&mid=2652864498&idx=1&sn=6bdb92b5950eb1fe1a257254dee69145&chksm=844bbe37b33c3721cc232127bf19d282c865073dd9786ca9b4db474dbee867f9f9935fd5f6ee&mpshare=1&scene=1&srcid=08239wJdvDgdLSYGhqiVQENi&key=1a8f9280f573accc2818a7b62558d4c260059787807a97d4607556335cc198da378d26398bd237bf54e8bb0e403b861f88d6d423ef0a5425df0a3d23bf1da23018b33f9a18e0bc5a3f50f0b07fb6ec96&ascene=0&uin=MTA5NTQxNTc1&devicetype=iMac+MacBookPro11%2C4+OSX+OSX+10.11.6+build(15G1611)&version=12020810&nettype=WIFI&fontScale=100&pass_ticket=uGchUv3CviAcxUhqpBB0q1c6U%2F2Zl06u%2BEzBOgEjolE%3D',
    ],
    'start_num': 0
    'elem': 'img',
    'attr': 'data-src',
    'out_dir': 'temp/',
}


def main(webpages, start_num=0, elem='img', attr='data-src', out_dir='temp/'):
    i = start_num
    for webpage in webpages:
        soup = BeautifulSoup(requests.get(webpage).text, 'html.parser')
        for img in soup.find_all(elem):
            src = img.get(attr)
            if src:
                r = requests.get(src)
                fn = '{0}{1}.jpg'.format(out_dir, i)
                with open(fn, 'wb') as f:
                    print('Downloading {}...'.format(fn))
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                i += 1


if __name__ == '__main__':
    main(**config)
