# my own modules
from email_message import EmailMessage
from online_store_item import OnlineShopItem

shop_item = OnlineShopItem()
shop_item.scrape_price()
lower_price: bool = shop_item.is_current_lower_than_preset_price()

emailing = EmailMessage(current_price=shop_item.current_price,
                        preset_price=shop_item.preset_price)

emailing.send_message(lower_than_preset=lower_price)
