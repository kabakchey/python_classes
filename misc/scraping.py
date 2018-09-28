import requests
import lxml
import lxml.html as lxml_html
import csv

from pprint import pprint as pp


# Links:
# https://habr.com/post/280238/
# https://www.youtube.com/watch?v=ind-mugxMxk
# https://www.youtube.com/watch?v=OJ8isyws2yw&list=PL5tcWHG-UPH1fnJw-BvBiiiPUPm1LUKsm&index=4


def xpath_demo():
    test = '''
        <html>
            <body>
                <div class="first_level">
                    <h2 align='center'>one</h2>
                    <h2 align='left'>two</h2>
                </div>
                <h2>another tag</h2>
            </body>
        </html>
    '''
    tree = lxml_html.fromstring(test)
    pp(tree.xpath('//h2'))
    pp(tree.xpath('//h2[@align]'))
    pp(tree.xpath('//h2[@align="center"]'))

    div_node = tree.xpath('//div')[0]
    pp(div_node.xpath('.//h2'))


def simple_fetch(url):
    page = requests.get(url)
    print(page.content[:100])

    tree = lxml_html.fromstring(page.content)
    print(type(tree), tree)
    pp(lxml.etree.tostring(tree))

    pp(tree.xpath('//a/@href'))
    pp(tree.xpath('//div[@class="quote"]/span[@itemprop="text"]/text()'))
    pp(tree.xpath('//div[@class="quote"]/span/small[@class="author"]/text()'))


def fetch_all_quotes(url, filepath):
    def _fetch_page(url):
        print('Fetching page %s ...' % url)
        page = requests.get(url)
        tree = lxml.html.fromstring(page.content)
        qoutes = tree.xpath('//div[@class="quote"]/span[@itemprop="text"]/text()')
        authors = tree.xpath('//div[@class="quote"]/span/small[@class="author"]/text()')

        data = zip(qoutes, authors)
        next_urls = []

        links = tree.xpath('//a/@href')
        if links:
            next_urls += [link for link in links if link.startswith('/page/')]

        return data, next_urls


    def _fetch_tree(url):
        visited_pages = []
        next_urls = ['/']

        for next_url in next_urls:
            next_url = url + next_url
            if next_url not in visited_pages:
                data, new_next_urls = _fetch_page(next_url)
                visited_pages.append(next_url)
                next_urls.extend(new_next_urls)
                yield data


    with open(filepath, 'w+') as csv_file:
        writer = csv.DictWriter(csv_file, ['qoute', 'author'])
        writer.writeheader()

        for data in _fetch_tree(url):
            for qoute, author in data:
                writer.writerow({'qoute': qoute,
                                 'author': author})


if __name__ == '__main__':
    xpath_demo()
    simple_fetch('http://quotes.toscrape.com')
    fetch_all_quotes('http://quotes.toscrape.com', 'qoutes.csv')

