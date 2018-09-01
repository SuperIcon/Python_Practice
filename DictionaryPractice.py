def count_products(data):
    dist = {}
    new = []
    for product in data:
        new = product.split()
        if new[0] in dist:
            dist[new[0]] = dist[new[0]] + int(new[1])
        else:
            dist[new[0]] = int(new[1])
    return dist


dist = {}
datas = ['麥香奶茶 2', '御飯糰 1', '可可 1', '麥香奶茶 1']
print(datas)
dist = count_products(datas)
print(dist)