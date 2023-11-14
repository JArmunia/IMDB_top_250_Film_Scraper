# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImdbscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # field_names = adapter.field_names()
        # for field_name in field_names:
        #     if field_name != "description":
        #         value = adapter.get(field_name)
        #         adapter[field_name] = value.strip()

        # lowercase_keys = ["category","product_type"]
        # for lowercase_key in lowercase_keys:
        #     adapter[lowercase_key] = adapter.get(lowercase_key).lower()

        # price_keys = ["price","price_excl_tax","price_incl_tax", "tax"]
        # for price_key in price_keys:
        #     adapter[price_key] = float(adapter.get(price_key).replace("£",""))
        

        # availability_string = adapter.get("availability")
        # split_string_array = availability_string.split("(")
        # if len(split_string_array) < 2:
        #     adapter["availability"] = 0
        # else:
        #     availability_number = split_string_array[1].split(" ")[0]
        #     adapter["availability"] = int(availability_number)

        # num_reviews_string = adapter.get("num_reviews")
        # adapter["num_reviews"] = int(num_reviews_string)

        # stars_string = adapter.get("stars")
        # split_stars_array = stars_string.split(" ")
        # stars_text_value = split_stars_array[1].lower()

        # if stars_text_value == "zero":
        #     adapter["stars"] = 0
        # elif stars_text_value == "one":
        #     adapter["stars"] = 1
        # elif stars_text_value == "two":
        #     adapter["stars"] = 2
        # elif stars_text_value == "three":
        #     adapter["stars"] = 3
        # elif stars_text_value == "four":
        #     adapter["stars"] = 4
        # elif stars_text_value == "five":
        #     adapter["stars"] = 5
        # else:
        #     adapter["stars"] = -1
        print("********************** item **********************")
        print(item)
        return item