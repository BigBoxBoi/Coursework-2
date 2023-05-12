from .models import Products
from . import db
from .models import Products
from . import db


def check_and_insert_product(name, description, price, carbon_footprint):
    products = Products.query.filter_by(name=name).first()
    if products is None:
        products = Products(name=name, description=description, price=price, carbon_footprint=carbon_footprint)
        db.session.add(products)
        db.session.commit()
    return products

def insert_products():
    check_and_insert_product("RegularChair", "Introducing our Regular Chair, a versatile and functional piece of furniture suitable for any space. With its classic design and sturdy construction, this chair provides a comfortable seating option for any activity. The chair features four legs and a supportive backrest, and is available in a variety of materials including wood, metal, plastic, and upholstery fabrics. Whether used in a home, office, or public setting, our Regular Chair is a reliable and practical choice for all your seating needs. Order yours today and enjoy the comfort and style of this timeless piece.", 20, 70)
    check_and_insert_product("PremiumChair", "Elevate your seating experience with our PremiumChair - order now and enjoy the ultimate in comfort and style. But be warned - some say the chair has a way of making you never want to leave your seat.", 3000, 200)
    check_and_insert_product("BigChair", "Introducing our BigChair - a spacious and comfortable seating option perfect for those who like to spread out and relax. With its large dimensions and plush cushioning, this chair provides a cozy and inviting space to unwind after a long day. But be warned, some say that sitting in the BigChair for too long can make you feel like you're sinking into an alternate dimension. Don't believe us? Try it for yourself and see if you're up for the challenge of this otherworldly chair. Available in a variety of colors and materials to match any decor, the BigChair is the ultimate in relaxation", 100, 200)
    check_and_insert_product("PlasticChair", "Introducing the PlasticChair - a functional seating option at an unbeatable price. We must be transparent with our customers and acknowledge that the production of this chair involves the use of plastic, a material that has been linked to environmental degradation and pollution. Some estimates suggest that the PlasticChair may contribute to as much as 10 percent of the plastic pollution in our oceans and landfills. But don not let that stop you from enjoying the unbeatable affordability and convenience of the PlasticChair - after all, we all have to sit somewhere, right?", 10, 1000)
    check_and_insert_product("MeatChair", "With the marvels that are modern preservatives, we are the first to bring to market a chair made entirely of flesh; we guarantee your money back with an 8 month warantee and promise our materials are all ethically sourced from more than willing participants.", 70, -80000)
    check_and_insert_product("WannabeChair", "His name is Andrew, Andrew grew up with no chairs in his home and was awestruck the moment he saw one and now through our employment seeks to fulfill his dream!", 20, 1600)
    check_and_insert_product("GhostChair", "Introducing the Ghost Chair - a transparent and ethereal seating option perfect for modern and minimalist decor. With its see-through construction and clean lines, this chair seamlessly blends into any space. But don't let its transparent appearance fool you - some say that the Ghost Chair is haunted by spirits of chairs past. Whether you believe in ghost stories or not, the Ghost Chair is a stylish and functional seating option that is sure to make a statement in any room.", 299.99, 50)
    check_and_insert_product("ZenChair", "The ZenChair is a sleek and stylish seating option that's designed to help you find your inner peace. With its ergonomic design and comfortable cushioning, this chair provides the perfect support for your body as you meditate, read, or simply relax. The ZenChair features a minimalist aesthetic that complements any decor, and its sturdy construction ensures that it will last for years to come. Treat yourself to the ultimate relaxation experience with the ZenChair.", 500, 100)