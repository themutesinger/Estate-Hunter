def pack_ad_to_dict(
    *,
    title,
    price,
    description,
    url,
    address,
    image,
    area
):
    return {
        'title': title,
        'price':price,
        'description': description,
        'url': url,
        'address': address,
        'image': image,
        'area': area
    }